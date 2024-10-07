# Bouncing Ball Simulation

## Overview
This project simulates the motion of a bouncing ball under the influence of gravity using Python. It helps students learn how basic physics concepts like gravity, velocity, and energy loss can be applied to programming.

In the **graph simulation**, we visualize the ball's position over time using the `matplotlib` library.

## Project Structure
- **student_files/**: Contains files for students to complete the exercises.
- **master_files/**: Contains the full working solutions.
- **graph_simulation/**: Contains the bouncing ball simulation with real-time graph visualization.

## Graph Simulation
In the `graph_simulation/` folder, we visualize the ball's bouncing motion in real-time using `matplotlib`.

### Setup: Installing Matplotlib Using Virtual Environment

To run the graph simulation, you’ll need to install the required dependencies like `matplotlib`. We recommend setting up a **virtual environment** to keep your project dependencies isolated.

### Steps to Set Up the Virtual Environment

1. **Create a Virtual Environment**:
   Open your terminal and navigate to the project directory. Then run the following command to create a virtual environment:
   ```bash
   python3 -m venv venv
2. **Activate the Virtual Environment**:
    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

3. **Install the Required Packages: Once the virtual environment is activated, you can install matplotlib**:

    ```bash
    pip3 install matplotlib
    ```

4. **Run the Graph Simulation: After installing the dependencies, you can run the bouncing ball simulation with graph visualization**:
    ```bash
    python3 graph_simulation/bouncing_ball_with_graph.py
    ```

5. **Deactivate the Virtual Environment: When you’re done, deactivate the virtual environment by running**:

    ```bash
    deactivate
    ```