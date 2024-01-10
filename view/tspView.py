class TSPView:
    def __init__(self, root, canvas, slider_label, num_points_slider):
        self.root = root
        self.canvas = canvas
        self.slider_label = slider_label
        self.num_points_slider = num_points_slider

    def draw_cities_and_solution(self, cities, best_order):
        # Draw points on the canvas and connect them with lines
        for i in range(len(best_order) - 1):
            start_city = cities[best_order[i]]
            end_city = cities[best_order[i + 1]]

            LINE_COLOR = '#A895FF'
            self.canvas.create_line(start_city.x, start_city.y,
                                    end_city.x, end_city.y, 
                                    width=2,
                                    fill=LINE_COLOR)
            
            POINT_OUTLINE = '#E4E5FF'
            POINT_COLOR = '#1F0068'
            self.canvas.create_oval(start_city.x - 5, start_city.y - 5,
                                    start_city.x + 5, start_city.y + 5,
                                    width=3,
                                    outline=POINT_OUTLINE,
                                    fill=POINT_COLOR)
