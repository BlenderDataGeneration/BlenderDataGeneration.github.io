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
        n_renders = self.calculate_n_renders(rot_step)
        print('Number of renders to create:', n_renders)

        accept_render = input('\nContinue?[Y/N]:  ')

        if accept_render == 'Y':
            report_file_path = self.labels_filepath + '/progress_report.txt'
            zmin = int(self.camera_z_limits[0] * 10)
            zmax = int(self.camera_z_limits[1] * 10)

            render_counter = -3
            rotation_step = rot_step

            report = open(report_file_path, 'w')

            for d in range(zmin, zmax + 1, 2):
                self.camera.location = (0, 0, d / 10)
                render_counter += 1
                min_beta = (-1) * self.beta_limits[0] + 90
                max_beta = (-1) * self.beta_limits[1] + 90

                for beta in range(min_beta, max_beta + 1, rotation_step):
                    beta_r = 90 - beta
                    render_counter += 1

                    for gamma in range(self.gamma_limits[0], self.gamma_limits[1] + 1, rotation_step):
                        render_counter += 1
                        axis_rotation = (m.radians(beta_r), 0, m.radians(gamma))
                        # print('Axis rotation at:', axis_rotation)
                        self.axis.rotation_euler = axis_rotation

                        ## Configure lighting
                        energy1 = random.randint(0, 30)
                        self.light_1.data.energy = energy1
                        energy2 = random.randint(4, 20)
                        self.light_2.data.energy = energy2

                        ## Generate render
                        self.render_blender(render_counter)

                        ## Output Labels
                        text_file_name = self.labels_filepath + '/' + str(render_counter) + '.txt'
                        text_file = open(text_file_name, 'w+')
                        text_coordinates = self.get_all_coordinates(self.xpix * self.percentage * 0.01,
                                                                    self.ypix * self.percentage * 0.01)
                        splitted_coordinates = text_coordinates.split('\n')[:-1]
                        text_file.write('\n'.join(splitted_coordinates))
                        text_file.close()

                        ## Show progress on batch of renders
                        print('Progress =', str(render_counter - 15627) + '/' + str(n_renders))
                        report.write('Progress: ' + str(render_counter) + ' Rotation: ' + str(axis_rotation) + ' z_d: ' + str(d / 10) + '\n')

            report.close()

        else:
            print('Aborted rendering operation')
            pass

    def get_all_coordinates(self, resx, resy):
        main_text_coordinates = ''
        for i, obj in enumerate(self.objects):
            b_box = self.find_bounding_box(obj)
            if b_box:
                text_coordinates = self.format_coordinates(b_box, i, resx, resy)
                main_text_coordinates = main_text_coordinates + text_coordinates

        return main_text_coordinates

    def format_coordinates(self, coordinates, classe, resx, resy):
        if coordinates:
            x1 = (coordinates[0][0])
            x2 = (coordinates[1][0])
            y1 = (1 - coordinates[1][1])
            y2 = (1 - coordinates[0][1])

            # print('minX:', x1, 'minY:', y1, '\nmaxX:', x2, 'maxY:', y2)
            txt_coordinates = self.obj_names[classe].replace(' ', '_') + ' ' + str(x1 * resx) + ' ' + str(
                y1 * resy) + ' ' + str(x2 * resx) + ' ' + str(y2 * resy) + '\n'

            return txt_coordinates

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
        # Define random parameters
        random.seed(random.randint(1,1000))
        self.xpix = random.randint(500, 1500)
        self.ypix = random.randint(500, 1500)
        self.percentage = random.randint(50, 100)
        samples = random.randint(25, 100)

        # Render images
        image_name = str(count_f_name) + '.png'
        self.export_render(self.xpix, self.ypix, self.percentage, samples, self.images_filepath, image_name)


    def export_render(self, res_x, res_y, res_per, samples, file_path, file_name):
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



r = Render()
r.set_camera()
r.main_rendering_loop(5)
