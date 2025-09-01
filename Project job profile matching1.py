import tkinter as tk
from tkinter import messagebox, font
from PIL import ImageTk, Image  # Import Pillow for images


# Function to match user profile with job profiles and open a new window for job details
def match_jobs():
    # Get user input
    user_skills = set(skill_entry.get().strip().lower().split(','))
    user_experience = int(experience_entry.get())
    user_location = location_entry.get().strip().lower()
    user_salary = salary_entry.get().strip()


    # Define the job profiles with company names and terms
    jobs = [
        (1, "Data head", "Develop and maintain software applications.", "IT", "Remote", "60k-100k", "Python, Java, SQL, Git", 3, "Google", "Full-time job","Master’s degree in a relevant field."),
        (2, "Data Analyst", "We are looking for a skilled Data Analyst to gather, process, and analyze data, providing insights that support key business decisions.he ideal candidate will be proficient in data mining, statistical analysis, and visualization,", "Data Science", "New York", "50k-80k", "SQL, Python, Tableau, Statistics", 2, "HCL", "Full-time/Part-time job","Master’s or Ph.D. in Data Science or a related field."),
        (3, 'Data Engineer',"We are looking for an experienced Data Engineer to design, build, and maintain the infrastructure required for optimal extraction, transformation, and loading (ETL) of data from a wide variety of sources. The ideal candidate will have a strong understanding of database architecture", "Data Science", "New York", "50k-80k", "SQL, Python, Tableau, Statistics", 2, "Amazon", "Full-time job","Master’s degree in a relevant field."),
        (4, "Data Scientist","We are seeking a Data Scientist to apply advanced data modeling techniques to extract valuable insights from large datasets, driving business strategy and decision-making. The ideal candidate will be experienced in machine learning, statistica analysis.", "data science", "New York", "50k-80k", "SQL, Python, Tableau, Statistics", 2, "Microsoft", "Work from home","Bachelor’s degree in Computer Science, Information Technology, or related field."),
        (5, 'Data Scientist', 'Extract insights from large datasets.', 'Data Science', "New ", "50k-80k", "SQL, Python, Tableau, Statistics", 4, "Microsoft", "Terms and conditions for Software Engineer at XYZ Corp","Bachelor’s degree in Computer Science, Information Technology, or related field.")  
        # Add more job profiles with company names and terms here...
    ]

    matching_jobs = []

    for job in jobs:
        # Unpack all 10 values (job ID, title, description, department, location, salary, skills, experience, company, job_type,qualifications)
        job_id, job_title, job_description, department, location, salary_range, required_skills, required_experience, company, job_type,qualifications = job
        job_skills = set(required_skills.lower().split(', '))

        # Check for matches
        skill_match = len(user_skills.intersection(job_skills)) / len(job_skills) >= 0.5
        experience_match = user_experience >= required_experience
        location_match = user_location == location.lower()
        salary_match = user_salary == salary_range

        if skill_match and experience_match and location_match and salary_match :
            matching_jobs.append(job)

    # Open a new window to show job details
    show_job_details(matching_jobs)


# Function to display detailed job information in a new window3
def show_job_details(matching_jobs):
    if not matching_jobs:
        messagebox.showinfo("No Matches", "No matching jobs found for your profile.")
        return

    # Create a new window for job details
    job_window = tk.Toplevel(root)
    job_window.title("Matching Job Details")
    job_window.geometry("1000x600")
    job_window.config(bg="#ffffff")

    header_font = font.Font(family='Times new roman', size=24 , weight='bold', underline=True)
    detail_font = font.Font(family='Times new roman', size=11)

    tk.Label(job_window, text="MATCHING JOBS", font=header_font, fg="#00796b", bg="#ffffff").pack(pady=20)

    for job in matching_jobs:
        job_id, job_title, job_description, department, location, salary_range, required_skills, required_experience, company, job_type,qualifications = job

        job_frame = tk.Frame(job_window, bg="#e0f7fa", bd=2, relief="solid")
        job_frame.pack(fill=tk.X, padx=20, pady=10)

        # Job title and company
        tk.Label(job_frame, text=f"Job Title: {job_title}", font=detail_font, fg="#00796b", bg="#e0f7fa").pack(anchor="w", padx=10, pady=2)
        tk.Label(job_frame, text=f"Company: {company}", font=detail_font, fg="#004d40", bg="#e0f7fa").pack(anchor="w", padx=10, pady=2)

        # Job location, salary, and description
        tk.Label(job_frame, text=f"Location: {location.capitalize()}", font=detail_font, fg="#004d40", bg="#e0f7fa").pack(anchor="w", padx=10, pady=2)
        tk.Label(job_frame, text=f"Salary Range: {salary_range}", font=detail_font, fg="#004d40", bg="#e0f7fa").pack(anchor="w", padx=10, pady=2)
        tk.Label(job_frame, text=f"Description: {job_description}", font=detail_font, fg="#004d40", bg="#e0f7fa", wraplength=1400, justify="left").pack(anchor="w", padx=10, pady=2)

        # Terms and Conditions
        tk.Label(job_frame, text=f"Job Type: {job_type}", font=detail_font, fg="#00796b", bg="#e0f7fa", wraplength=800, justify="left").pack(anchor="w", padx=10, pady=5)
        tk.Label(job_frame, text=f"qualifications: {qualifications}", font=detail_font, fg="#00796b", bg="#e0f7fa", wraplength=800, justify="left").pack(anchor="w", padx=10, pady=5)



# Set up the GUI
root = tk.Tk()
root.title("JOB PROFILE MATCHING (USER)")
root.geometry("1000x800")
root.config(bg="#e0f7fa")


# Load and set background image
background_image = Image.open("C:\\Users\\SHIKSHA\\Pictures\\사진\\bg man.jpg")
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set custom fonts
header_font = font.Font(family='Helvetica', size=26, weight='bold', underline=True)
label_font = font.Font(family='Helvetica', size=20, weight='bold')
entry_font = font.Font(family='Helvetica', size=14)
button_font = font.Font(family='Helvetica', size=20, weight='bold')

# Header
header = tk.Label(root, text="JOB PROFILE MATCHING (USER)", font=header_font, fg="#00796b", bg="#e0f7fa")
header.place(x=200, y=15)

# Form
form_frame = tk.Frame(root, bg="#e0f7fa")
form_frame.place(x=100, y=100)

tk.Label(form_frame, text="Skills (comma-separated):", font=label_font, fg="#004d40", bg="#e0f7fa").grid(row=0, column=0, sticky=tk.W, padx=20, pady=20)
skill_entry = tk.Entry(form_frame, width=40, font=entry_font, bd=4, relief="solid")
skill_entry.grid(row=0, column=1, padx=20, pady=20)

tk.Label(form_frame, text="Years of Experience:", font=label_font, fg="#004d40", bg="#e0f7fa").grid(row=1, column=0, sticky=tk.W, padx=20, pady=20)
experience_entry = tk.Entry(form_frame, width=40, font=entry_font, bd=4, relief="solid")
experience_entry.grid(row=1, column=1, padx=20, pady=20)

tk.Label(form_frame, text="Preferred Location:", font=label_font, fg="#004d40", bg="#e0f7fa").grid(row=2, column=0, sticky=tk.W, padx=20, pady=20)
location_entry = tk.Entry(form_frame, width=40, font=entry_font, bd=4, relief="solid")
location_entry.grid(row=2, column=1, padx=20, pady=20)

tk.Label(form_frame, text="Preferred Salary Range:", font=label_font, fg="#004d40", bg="#e0f7fa").grid(row=3, column=0, sticky=tk.W, padx=20, pady=20)
salary_entry = tk.Entry(form_frame, width=40, font=entry_font, bd=4, relief="solid")
salary_entry.grid(row=3, column=1, padx=20, pady=20)

# Match button
match_button = tk.Button(root, text="Find Matching Jobs", font=button_font, fg="white", bg="#00796b", relief="raised", command=match_jobs)
match_button.place(x=250,y=520)

root.mainloop()
