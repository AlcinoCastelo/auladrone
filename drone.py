from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

if __name__ == '__main__':

    sim_key = ' e6d5ff04-f23c-4cfb-82ae-943df387ba56'
    distance = 40
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.fly_forward(distance, 'in')
        drone.fly_left(distance, 'in')
        drone.fly_backward(distance, 'in')
        drone.fly_right(distance, 'in')
        drone.flip_backward()
        drone.land()
