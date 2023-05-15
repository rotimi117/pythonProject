
heights_inches = [69, 77, 54]
heights_meters = [(x, x * 0.0254) for x in heights_inches]

heights_inches = [69, 77, 54]
heights_meters = list(map(lambda x: (x, x * 0.0254), heights_inches))
