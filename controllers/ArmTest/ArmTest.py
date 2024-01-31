#!/usr/bin/env python3  

from controller import Supervisor
from controller import Robot
from controller import Motor

#from controller import Device
import math
import rospy
import time

def main():

    # Obtener el nodo del robot
    robot = Supervisor()

    # Obtener una referencia a un dispositivo en tu robot 
    robot_node = robot.getFromDef("ROBOT") 
    
    # Obtener el motor rotacional 
    motor_1 = robot.getDevice("m1_continuous")
    motor_2 = robot.getDevice("m2")
    motor_3 = robot.getDevice("m3")
    motor_4 = robot.getDevice("m4")
    motor_5 = robot.getDevice("m5")
    
    # Obtener los sensores y habilitarlos 
    
    sensor_1 = robot.getDevice("m1_continuous_sensor")
    sensor_2 = robot.getDevice("m2_sensor")
    sensor_3 = robot.getDevice("m3_sensor")
    sensor_4 = robot.getDevice("m4_sensor")
    sensor_5 = robot.getDevice("m5_sensor")
    
    sensors = [sensor_1, sensor_2, sensor_3, sensor_4, sensor_5]
    for sensor in sensors:
        sensor.enable(10)

    # Get time Step
    time_step = int(robot.getBasicTimeStep()) 

    # Tiempo actual al comenzar el bucle
    start_time = time.time()

    # Duración deseada del bucle en segundos
    duration = 5

    # Bucle que se ejecuta durante aproximadamente 5 segundos
    while time.time() - start_time < duration and robot.step(time_step) != -1:
        motor_1.setPosition(0) 
        motor_2.setPosition(math.pi / 4) 
        motor_3.setPosition(0) 
        motor_4.setPosition(0) 
        motor_5.setPosition(0) 
        pass  # Solo para mantener el bucle activo

    print("Posicion Home alcanzada")

    # Configuracion para mover los motores por velocidad

    motor_1.setPosition(float('inf')) 
    motor_2.setPosition(float('inf')) 
    motor_3.setPosition(float('inf')) 
    motor_4.setPosition(float('inf')) 
    motor_5.setPosition(float('inf')) 

    motor_1.setVelocity(0.0)
    motor_2.setVelocity(0.0)
    motor_3.setVelocity(0.0)
    motor_4.setVelocity(0.0)
    motor_5.setVelocity(0.0)

    # Imprimir información sobre el motor y el sensor
    print("Información del motor 'm1':")
    print("  - Nombre:", motor_1.getName())
    print("  - Velocidad máxima:", motor_1.getMaxVelocity())
    print("  - Posición mínima:", motor_1.getMinPosition())
    print("  - Posición máxima:", motor_1.getMaxPosition())
    print("  - Torque máximo:", motor_1.getMaxTorque())
    
    print("\nInformación del sensor de posición 'm2_sensor':")
    print("  - Nombre:", sensor_2.getName())
    
    print("Posición actual del motor 'm2':", sensor_2.getValue())
    

    # Sample Time Defintion
    sample_time = 0.01

    # Frequency of the simulation
    hz = int(1/sample_time)
   
    # Time defintion
    rate = rospy.Rate(10)

    # INICIA BUCLE PRINCIPAL    
    while robot.step(time_step) != -1:
        tic = time.time()

        motor_1.setVelocity(0.1)
        motor_2.setVelocity(0.0)
        motor_3.setVelocity(0.0)
        motor_4.setVelocity(0.0)
        motor_5.setVelocity(0.0)

        print("Posición actual del motor 'm2':", sensor_2.getValue())        
        
        #print("Posición del robot:", position)
        rate.sleep()
        toc = time.time() - tic 
    
        print("FPS: {:.2f} Hz".format(1/toc), end='\r')

if __name__ == '__main__':
    try:
        # Node Initialization
        rospy.init_node("vision_system",disable_signals=True, anonymous=True)

        # Simulation 
        main()

    except(rospy.ROSInterruptException, KeyboardInterrupt):
        print("Error System")
        pass
    else:
        print("Complete Execution")
        pass
