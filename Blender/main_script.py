## Import all relevant libraries
import bpy
import numpy as np
import time
import math as m
import os
import random

class Render:
    def __init__(self):
        ## Scene information
        # Define the scene information
        self.scene = bpy.data.scenes['Scene']
        # Define the information relevant to the <bpy.data.objects>
        self.camera = bpy.data.objects['Camera']
        self.axis = bpy.data.objects['Empty']
        self.light_1 = bpy.data.objects['Light']
        self.light_2 = bpy.data.objects['Light2']
        self.obj_names = ['Fleur rose', 'Carre bleu', 'Etoile verte', 'Hexagone jaune', 'Losange orange',
                          'Ovale rose', 'Rectangle bleu', 'Rond vert', 'Triangle eq orange']
        self.objects = self.create_objects() # Create list of bpy.data.objects from bpy.data.objects[1] to bpy.data.objects[N]

        ## Render information
        self.camera_z_limits = [0.3, 1] # Define range of heights z that the camera is going to pan through
        self.beta_limits = [80, -80] # Define range of beta angles that the camera is going to pan through
        self.gamma_limits = [0, 360] # Define range of gamma angles that the camera is going to pan through
        
        ## Output information
        # Input your own preferred location for the images
        self.images_filepath = 'C:/Users/Federico Arenas/Desktop/GitHubrepo/BlenderDataGeneration.github.io/Blender/Data'
        # Input your own preferred location for the labels
        self.labels_filepath = 'C:/Users/Federico Arenas/Desktop/GitHubrepo/BlenderDataGeneration.github.io/Blender/Data/Labels'

    def create_objects(self): # This function creates a list of all the <bpy.data.objects> 
        objs = []
        for obj in self.obj_names:
            objs.append(bpy.data.objects[obj])
        
        return objs

    def main_rendering_loop(self, rot_step):
        '''
        This function represent the main algorithm explained in the Tutorial, it accepts the
        rotation step as input, and outputs the images and the labels to the above specified locations.
        '''
        ## Calculate the number of images and labels to generate
        n_renders = self.calculate_n_renders(rot_step) # Calculate number of images
        print('Number of renders to create:', n_renders)

        accept_render = input('\nContinue?[Y/N]:  ') # Ask whether to procede with the data generation

        if accept_render == 'Y': # If the user inputs 'Y' then procede with the data generation
            # Create .txt file that record the progress of the data generation
            report_file_path = self.labels_filepath + '/progress_report.txt' 
            report = open(report_file_path, 'w')
            # Multiply the limits by 10 to adapt to the for loop
            zmin = int(self.camera_z_limits[0] * 10) 
            zmax = int(self.camera_z_limits[1] * 10)
            # Define a counter to name each .png and .txt files that are outputted
            render_counter = -3
            # Define the step with which the pictures are going to be taken
            rotation_step = rot_step

            # Begin nested loops
            for d in range(zmin, zmax + 1, 2): # Loop to vary the height of the camera
                render_counter += 1 # Update the counter 
                ## Update the height of the camera 
                self.camera.location = (0, 0, d/10) # Divide the distance z by 10 to re-factor current height

                # Refactor the beta limits for them to be in a range from 0 to 360 to adapt the limits to the for loop
                min_beta = (-1) * self.beta_limits[0] + 90 
                max_beta = (-1) * self.beta_limits[1] + 90

                for beta in range(min_beta, max_beta + 1, rotation_step): # Loop to vary the angle beta
                    beta_r = 90 - beta # Re-factor the current beta
                    render_counter += 1 # Update the counter

                    for gamma in range(self.gamma_limits[0], self.gamma_limits[1] + 1, rotation_step): # Loop to vary the angle gamma
                        render_counter += 1 # Update the counter
                        
                        ## Update the rotation of the axis
                        axis_rotation = (m.radians(beta_r), 0, m.radians(gamma)) 
                        self.axis.rotation_euler = axis_rotation # Assign rotation to <bpy.data.objects['Empty']> object

                        ## Configure lighting
                        energy1 = random.randint(0, 30) # Grab random light intensity
                        self.light_1.data.energy = energy1 # Update the <bpy.data.objects['Light']> energy information
                        energy2 = random.randint(4, 20) # Grab random light intensity
                        self.light_2.data.energy = energy2 # Update the <bpy.data.objects['Light2']> energy information

                        ## Generate render
                        self.render_blender(render_counter) # Take photo of current scene and ouput the render_counter.png file

                        ## Output Labels
                        text_file_name = self.labels_filepath + '/' + str(render_counter) + '.txt' # Create label file name
                        text_file = open(text_file_name, 'w+') # Open .txt file
                        text_coordinates = self.get_all_coordinates(self.xpix * self.percentage * 0.01,
                                                                    self.ypix * self.percentage * 0.01) # Get formatted coordinates of the bounding boxes of all the objects in the scene
                        splitted_coordinates = text_coordinates.split('\n')[:-1] # Delete last '\n' in coordinates
                        text_file.write('\n'.join(splitted_coordinates)) # Write the coordinates to the text file and output the render_counter.txt file
                        text_file.close() # Close the .txt file corresponding to the label
 
                        ## Show progress on batch of renders
                        print('Progress =', str(render_counter) + '/' + str(n_renders))
                        report.write('Progress: ' + str(render_counter) + ' Rotation: ' + str(axis_rotation) + ' z_d: ' + str(d / 10) + '\n')

            report.close() # Close the .txt file corresponding to the report

        else: # If the user inputs anything else, then abort the data generation
            print('Aborted rendering operation')
            pass

    def get_all_coordinates(self, resx, resy):
        '''
        This function takes the width and height of the image and outputs
        the complete string with the coordinates of all the objects in view in 
        the current image
        '''
        main_text_coordinates = '' # Initialize the variable where we'll store the coordinates
        for i, obj in enumerate(self.objects): # Loop through all of the objects
            b_box = self.find_bounding_box(obj) # Get current object's coordinates
            if b_box: # If find_bounding_box() doesn't return None
                text_coordinates = self.format_coordinates(b_box, i, resx, resy) # Reformat coordinates to YOLOv3 format
                main_text_coordinates = main_text_coordinates + text_coordinates # Update main_text_coordinates variables which each
                                                                                 # line corresponding to each class in the frame of the current image

        return main_text_coordinates # Return all coordinates

    def format_coordinates(self, coordinates, classe, img_width, img_height):
        '''
        This function takes as inputs the coordinates created by the find_bounding box() function, the current class,
        the image width and the image height and outputs the coordinates of the bounding box of the current class
        '''
        # If the current class is in view of the camera
        if coordinates: 
            ## Change coordinates reference frame
            x1 = (coordinates[0][0])
            x2 = (coordinates[1][0])
            y1 = (1 - coordinates[1][1])
            y2 = (1 - coordinates[0][1])

            ## Get final bounding box information
            width = (x2-x1)  # Calculate the absolute width of the bounding box
            height = (y2-y1) # Calculate the absolute height of the bounding box
            # Calculate the absolute center of the bounding box
            cx = x1 + (width/2) 
            cy = y1 + (height/2)

            ## Formulate line corresponding to the bounding box of one class
            txt_coordinates = str(classe) + ' ' + str(cx) + ' ' + str(cy) + ' ' + str(width) + ' ' + str(height) + '\n'

            return txt_coordinates

        # If the current class isn't in view of the camera, then pass
        else:
            pass

    def find_bounding_box(self, obj):
        """
        Returns camera space bounding box of the mesh object.

        Gets the camera frame bounding box, which by default is returned without any transformations applied.
        Create a new mesh object based on self.carre_bleu and undo any transformations so that it is in the same space as the
        camera frame. Find the min/max vertex coordinates of the mesh visible in the frame, or None if the mesh is not in view.

        :param scene:
        :param camera_object:
        :param mesh_object:
        :return:
        """
        """ Get the inverse transformation matrix. """
        matrix = self.camera.matrix_world.normalized().inverted()
        """ Create a new mesh data block, using the inverse transform matrix to undo any transformations. """
        mesh = obj.to_mesh(preserve_all_data_layers=True)
        mesh.transform(obj.matrix_world)
        mesh.transform(matrix)
        """ Get the world coordinates for the camera frame bounding box, before any transformations. """
        frame = [-v for v in self.camera.data.view_frame(scene=self.scene)[:3]]
        lx = []
        ly = []

        for v in mesh.vertices:
            co_local = v.co
            z = -co_local.z
            if z <= 0.0:
                """ Vertex is behind the camera; ignore it. """
                continue
            else:
                """ Perspective division """
                frame = [(v / (v.z / z)) for v in frame]
            min_x, max_x = frame[1].x, frame[2].x
            min_y, max_y = frame[0].y, frame[1].y
            x = (co_local.x - min_x) / (max_x - min_x)
            y = (co_local.y - min_y) / (max_y - min_y)
            lx.append(x)
            ly.append(y)


        """ Image is not in view if all the mesh verts were ignored """
        if not lx or not ly:
            return None

        min_x = np.clip(min(lx), 0.0, 1.0)
        min_y = np.clip(min(ly), 0.0, 1.0)
        max_x = np.clip(max(lx), 0.0, 1.0)
        max_y = np.clip(max(ly), 0.0, 1.0)

        """ Image is not in view if both bounding points exist on the same side """
        if min_x == max_x or min_y == max_y:
            return None

        """ Figure out the rendered image size """
        render = self.scene.render
        fac = render.resolution_percentage * 0.01
        dim_x = render.resolution_x * fac
        dim_y = render.resolution_y * fac
        
        ## Verify there's no coordinates equal to zero
        coord_list = [min_x, min_y, max_x, max_y]
        if min(coord_list) == 0.0:
            indexmin = coord_list.index(min(coord_list))
            coord_list[indexmin] = coord_list[indexmin] + 0.0000001

        return (min_x, min_y), (max_x, max_y)

    def render_blender(self, count_f_name):
        '''
        This function takes as input the render_counter and 
        updates the photo information of the render
        '''
        # Define random parameters
        random.seed(random.randint(1,1000)) # Update the random seed
        self.xpix = random.randint(500, 1500) # Update x resolution as a number random number between 500 and 1500
        self.ypix = random.randint(500, 1500) # Update y resolution as a number random number between 500 and 1500
        self.percentage = random.randint(50, 100) # Update the resolution percentage of the image as a random percentage between 50% and 100%
        samples = random.randint(25, 100) # Update the render samples between 25 and 100

        # Render images
        image_name = str(count_f_name) + '.png' # Create file_name as 'render_counter.png'
        self.export_render(self.xpix, self.ypix, self.percentage, samples, self.images_filepath, image_name)


    def export_render(self, res_x, res_y, res_per, samples, file_path, file_name):
        '''
        This function takes the size x and y of the image, the resolution percentage, the samples of the render,
        the image path and the the image name, and outputs image named as 'file_name'
        '''
        bpy.context.scene.cycles.samples = samples
        self.scene.render.resolution_x = res_x
        self.scene.render.resolution_y = res_y
        self.scene.render.resolution_percentage = res_per
        self.scene.render.filepath =  file_path + '/' + file_name

        bpy.ops.render.render(write_still=True)

    def set_camera(self):
        self.axis.rotation_euler = (0, 0, 0)
        self.axis.location = (0, 0, 0)
        self.camera.location = (0, 0, 3)

    def calculate_n_renders(self, rotation_step):
        zmin = int(self.camera_z_limits[0] * 10)
        zmax = int(self.camera_z_limits[1] * 10)

        render_counter = 1
        rotation_step = rotation_step

        for d in range(zmin, zmax+1, 2):
            camera_location = (0,0,d/10)
            #print('Camera location at:', camera_location)
            render_counter +=1
            min_beta = (-1)*self.beta_limits[0] + 90
            max_beta = (-1)*self.beta_limits[1] + 90

            for beta in range(min_beta, max_beta+1,rotation_step):
                beta_r = 90 - beta
                render_counter +=1

                for gamma in range(self.gamma_limits[0], self.gamma_limits[1]+1,rotation_step):
                    render_counter += 1
                    axis_rotation = (beta_r, 0, gamma)

        return render_counter


if __name__ == '__main__':
    r = Render() # Initialize Render() class and define it as r
    r.set_camera() # Initialize all positions of the camera and the axis
    r.main_rendering_loop(5) # Start rendering with specified rotation step (rot_step)
