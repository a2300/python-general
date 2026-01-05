input_data = [10.1, 22.5, 33.3, -9999, 45.6, 50.0, -9999, 60.2]

sanitized_data = [value for value in input_data if value != -9999]
print("Sanitized Data:", sanitized_data)

sanitized_data_default = [value if value != -9999 else 0 for value in input_data]
print("Sanitized Data with Defaults:", sanitized_data_default)
