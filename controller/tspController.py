import tkinter
import random
from model.tspSolver import TSPSolver
from model.city import City
from view.tspView import TSPView

class TSPController:
    def __init__(self):
        # Create the main window
        self.root = tkinter.Tk()
        self.root.title("Traveling Salesman Problem (TSP) Visualization")

        # Set the window background color to indigo with opacity 0.8
        self.root.configure(bg='#3D26B1')
        self.root.resizable(width=0, height=0)
        self.root.attributes('-alpha',0.9)
        
        # Set the size of the main window
        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 700
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Create a canvas
        CANVAS_WIDTH = 580
        CANVAS_HEIGHT = 580
        BG_COLOR = '#3D26B1'
        self.canvas = tkinter.Canvas(self.root,
                                width=CANVAS_WIDTH,
                                height=CANVAS_HEIGHT,
                                bg=BG_COLOR)
        self.canvas.pack(fill=tkinter.BOTH, expand=False, padx=20, pady=20)  # Set pady to 10 for a 10-pixel space at the top

        # Set borderwidth and highlightthickness to zero to remove the border
        self.canvas.configure(borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        # Create a slider to adjust the number of cities
        LABEL_BG_COLOR = '#1F0068'
        self.slider_label = tkinter.Label(self.root, 
                                     text="Number of Cities:",
                                     bg=LABEL_BG_COLOR)
        self.slider_label.pack()

        SLIDER_MIN = 3
        SLIDER_MAX = 50
        SLIDER_INIT_VALUE = 5
        SLIDER_FOREGROUND_COLOR = '#ABAFFF'
        SLIDER_BG_COLOR = '#1F0068'
        self.num_cities_slider = tkinter.Scale(self.root, 
                                          from_=SLIDER_MIN, 
                                          to=SLIDER_MAX, 
                                          orient=tkinter.HORIZONTAL, 
                                          length=400,
                                          command=self.update_cities,
                                          foreground=SLIDER_FOREGROUND_COLOR, 
                                          bg=SLIDER_BG_COLOR)
        # Set initial value
        self.num_cities_slider.set(SLIDER_INIT_VALUE)  
        self.num_cities_slider.pack()

        # Initialize cities and distances
        self.initialize_cities()

        # Create the view
        self.view = TSPView(self.root, self.canvas, self.slider_label, self.num_cities_slider)

        # Draw initial cities and solve TSP
        self.view.draw_cities_and_solution(self.cities, self.best_order)

        # Run the Tkinter event loop
        self.root.mainloop()

    def initialize_cities(self):    
        self.num_cities = self.num_cities_slider.get()
        self.cities = [City(x=random.randint(20, 540),
                            y=random.randint(20, 540)) for _ in range(self.num_cities)]
        self.solver = TSPSolver(self.cities)

        ordered_cities, min_distance = self.solver.nearest_neighbor_tsp()
        self.best_order = ordered_cities
        self.minimum_distance = min_distance

    def update_cities(self, value):
        self.num_cities = int(value)
        self.cities = [City(x=random.randint(20, 540),
                            y=random.randint(20, 540)) for _ in range(self.num_cities)]
        self.solver = TSPSolver(self.cities)

        ordered_cities, min_distance = self.solver.nearest_neighbor_tsp()
        self.best_order = ordered_cities
        self.minimum_distance = min_distance

        # Clear canvas and redraw
        self.clear_and_redraw()

    def clear_and_redraw(self):
        # Clear canvas and redraw
        self.canvas.delete("all")
        self.view.draw_cities_and_solution(self.cities, self.best_order)
        