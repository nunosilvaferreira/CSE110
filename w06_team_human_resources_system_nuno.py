# Open the HR System file and read through it line by line
with open("hr_system.txt") as file:
    for line in file:
        # Strip leading and trailing whitespace
        line = line.strip()
        
        # Split the line into parts
        parts = line.split(" ")
        
        # Extract relevant data
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])  # Convert salary to a float
        
        # Calculate paycheck amount (twice a month payment)
        paycheck = salary / 24  # 24 pay periods in a year (bi-monthly)
        
        # Add bonus for Engineers
        if job_title.lower() == "engineer":
            paycheck += 1000  # Bonus for engineers
        
        # Display formatted output
        print(f"{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}")
