sunset = load_image("/content/111713392_2901319196658224_5294982908021128204_n.png")
clean_image = median(sunset, ball(3))
edge_detection_clean_image = edge_detection(clean_image)

threshold = 50
binary = (edge_detection_clean_image > threshold).astype(int)
