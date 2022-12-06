import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import glob
import os
import sys
import time

try:
    sys.path.append(glob.glob('PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
import random
import cv2
import skimage.measure as measure

#in synchronous mode, sensor data must be added to a queue
import queue

client = carla.Client('localhost', 2000)
client.set_timeout(11.0)


world = client.load_world('Town03')
settings = world.get_settings()
settings.fixed_delta_seconds = 0.05 #must be less than 0.1, or else physics will be noisy
#must use fixed delta seconds and synchronous mode for python api controlled sim, or else 
#camera and sensor data may not match simulation properly and will be noisy 
settings.synchronous_mode = True 
world.apply_settings(settings)

## weather 
weather = carla.WeatherParameters(
    cloudiness=20.0,
    precipitation=20.0,
    sun_altitude_angle=110.0)

world.set_weather(weather)

blueprints = world.get_blueprint_library().filter('*')
# for blueprint in random.sample(list(blueprints), 30):
#     print(blueprint.id)
#     for attr in blueprint:
#         print('  - {}'.format(attr))

actor_list = []

blueprint_library = world.get_blueprint_library()
bp = random.choice(blueprint_library.filter('vehicle')) # lets choose a vehicle at random

# lets choose a random spawn point
transform = random.choice(world.get_map().get_spawn_points()) 

[insert]

#spawn a vehicle
vehicle = world.spawn_actor(bp, transform) 
actor_list.append(vehicle)

vehicle.set_autopilot(True)

m= world.get_map()
waypoint = m.get_waypoint(transform.location)

#lets add more vehicles
for _ in range(0, 200):
    transform = random.choice(m.get_spawn_points())

    bp_vehicle = random.choice(blueprint_library.filter('vehicle'))

    # This time we are using try_spawn_actor. If the spot is already
    # occupied by another object, the function will return None.
    other_vehicle = world.try_spawn_actor(bp_vehicle, transform)
    if other_vehicle is not None:
        #print(npc)
        other_vehicle.set_autopilot(True)
        actor_list.append(other_vehicle)

blueprint_library = world.get_blueprint_library()
weirdobj_bp = blueprint_library.find('static.prop.fountain')
weirdobj_transform = random.choice(world.get_map().get_spawn_points())
weirdobj_transform = carla.Transform(carla.Location(x=230, y=195, z=40), carla.Rotation(yaw=180))
weird_obj = world.try_spawn_actor(weirdobj_bp, weirdobj_transform)
actor_list.append(weird_obj)

camera_bp = blueprint_library.find('sensor.camera.rgb')
# camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
camera_transform = carla.Transform(carla.Location(x=-5.5, z=2.8), carla.Rotation(pitch=-15))
camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)
image_queue = queue.Queue()
camera.listen(image_queue.put)
actor_list.append(camera)

dataset_dicts = []
global_count=0
timestamp = round(time.time())
for i in range(1000):
    #step
    world.tick()

    #rgb camera
    image = image_queue.get()

    
    if i%100==0:
        image.save_to_disk(f"test_images/{timestamp}/%06d.png" %(image.frame))

        # img = mpimg.imread(f"test_images/{timestamp}/%06d.png" %(image.frame))

    #drive vehicle to next waypoint on map
    waypoint = random.choice(waypoint.next(1.5))
    vehicle.set_transform(waypoint.transform)

