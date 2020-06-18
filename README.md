Generate synthetic data with Blender and Python
======
You can use the [editor on GitHub](https://github.com/BlenderDataGeneration/BlenderDataGeneration.github.io/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

- [Overview of the Project](#overview-of-the-project)
- [Blender scene setup](#blender-scene-setup)
  * [CAD Model import](#cad-model-import)
  * [Scene definition](#scene-defintion)
  * [Camera setting](#camera-setting)
  * [CAD Model import](#cad-model-import)
- [Blender scritping](#blender-scripting)
  * [Introduction to the blender console](#introduction-to-the-blender-console)
      + [Accessing scene information](#accessing-scene-information)
      + [Accessing object information](#accessing-object-information)
      + [Modifying object information](#modifying-object-information)
  * [Main algorithm to generate the training data](#main-procedure-to-generate-the-training-data)
  * [Rendering class initial definition](#rendering-class-initial-definition)
  * [Main function](#rendering-class-initial-definition)
      + [Get_text_coordinates function](#get_text_coordinates-function)
- [Test with YOLO and Google Colab](#test-with-yolo-and-google-colab)
  * [YOLOv3 on Colab](#yolov3-on-colab)
  * [Results obtained](#results-obtained)
    
<!-- toc -->


# **Overview of the Project**
Neque sitisquam volecae repelis doluptassin pore reium facearchita que vel eos nimpore et, quiatiis molut aut et quident pelibus am ditis nonsectati inctotatem reruptatet volo tem. Lique essi tem. Neque necto eos dolorectem simus ut volores ciatiosti net faccatemquo ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Realexample1.jpeg)  ![](Images/Realexample2.jpeg)  ![](Images/Realexample3.jpg)
![](Images/Realexample4.jpg)  ![](Images/Realexample5.jpg)  ![](Images/Realexample6.jpg)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

# **Blender scene setup**
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

## CAD Model import
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Catia_CAD_model.PNG)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Import_STIL_blender.PNG)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Scale_image_Blender.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Blender_CAD_model_import.PNG)

## Scene definition
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Define_materials_Blender.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Add_textures_Blender.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Light_setup_Blender.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Final_scene_Blender.png)

A complete guide made by Blender Guru on how to set the rendering configurations in Blender can be found [here](https://www.youtube.com/watch?v=ZTxBrjN1ugA) as well as the guide on setting the materials of each object in the scene that can be found [here](https://www.youtube.com/watch?v=5lr8QnR5WWU&t=414s). Finally, the complete guide on how to assign textures to an object in blender can be found [here](https://www.youtube.com/watch?v=r5YNJghc81U).

## Camera setting
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

The complete guide to how to set the camera to orbit around a specific object can be found [here](https://www.youtube.com/watch?v=ghCsEVj2CFE).

![](Images/Add_axis_Blender.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Parent_camera_to_axis_Blender.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Final_demo_parent_Blender.png)

# **Blender scritping**
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Scripting_console_Blender.png)

## Introduction to the blender console
### >> Accesing scene information
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

```
>>> bpy.data
<bpy_struct, BlendData at 0x000001C251997458>

>>> bpy.data.scenes
<bpy_collection[1], BlendDataScenes>

>>> bpy.data.scenes[0]
bpy.data.scenes['Scene']

>>> bpy.data.scenes[1]
Traceback (most recent call last):
  File "<blender_console>", line 1, in <module>
IndexError: bpy_prop_collection[index]: index 1 out of range, size 1

>>> scene = bpy.data.scenes[0]
>>> scene
bpy.data.scenes['Scene']

```
### >> Accesing object information
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

```
>>> bpy.data.objects
<bpy_collection[15], BlendDataObjects>

>>> bpy.data.objects[0]
bpy.data.objects['Camera']

>>> camera = bpy.data.objects['Camera']
>>> bpy.data.objects[1]
bpy.data.objects['Carre bleu']

>>> bpy.data.objects[2]
bpy.data.objects['Conteneur coupe']

>>> bpy.data.objects[3]
bpy.data.objects['Empty']

>>> axe = bpy.data.objects[3]
>>> axe
bpy.data.objects['Empty']

>>> camera
bpy.data.objects['Camera']

>>> carre_bleu = bpy.data.objects['Carre bleu']
>>> carre_bleu
bpy.data.objects['Carre bleu']

>>> bpy.data.objects['Light']
bpy.data.objects['Light']

>>> light1 = bpy.data.objects['Light']
>>> light2 = bpy.data.objects['Light2']
>>> light1
bpy.data.objects['Light']

>>> light2
bpy.data.objects['Light2']

```

### >> Modifying object information
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Modifying_objects_Blender.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

```
>>> axe.rotation_euler = (0,0,0)
>>> camera.location = (0,0,0.5)
>>> light1.energy = 50
>>> light1.data.energy = 50
>>> light2.data.energy = 0
```
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/After_scripting_changes_Blender.PNG)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Scripting_rotated_Blender.png)


## Main procedure to generate the training data
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Figure_environment_Blender.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Algorithm.png)

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur

![](https://media.giphy.com/media/RJmzbdJQdTRAwyeY0N/giphy.gif)

voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

![](Images/Expected_results.png)

## Rendering class initial definition
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

```
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
```

## Main algorithm to pan around the objects and take pictures
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

```
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
```

## Main function to extract labels from all objects in image
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

```
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
```

ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

## Results obtained from the data generation




# **Test with YOLO and Google Colab**
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?

```
>>> axe.rotation_euler = (0,0,0)
>>> camera.location = (0,0,0.5)
>>> light1.energy = 50
>>> light1.data.energy = 50
>>> light2.data.energy = 0
```

## YOLOv3 on Colab
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?


## Results obtained
ommo vollam fugitem corrumq uatende liquiam, apit ra volorrum laborpo repedigene nullest quidelit eiur audicia doluptaectur sit deria dolutem fugiae con plita del ipsam ilici debiti rerovides magnim non pa nimoles quasper spelliquo ma velent plis et is estotatur, voluptamet dionsequunt, aut audis et qui rem. Itas voluptatusci odi tectet aut alit liquate nonem facerum doluptur?
