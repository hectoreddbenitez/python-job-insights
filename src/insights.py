from .jobs import read


def get_unique_job_types(path):
    job_types = []
    """ jobs_list = jobs.read(path)"""
    jobs_list = read(path)
    for job in jobs_list:
        type = job["job_type"]
        if job_types.count(type) == 0:
            job_types.append(type)
    """qual é o erro nessa compreensão??
     job_types = [
         job
         for job in jobs_list if job_types.count(job["job_type"]) == 0
    ]"""
    return job_types


def filter_by_job_type(jobs, job_type):
    chosen_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            chosen_jobs.append(job)
    return chosen_jobs


def get_unique_industries(path):
    industry_types = []
    jobs_list = read(path)
    for job in jobs_list:
        type = job["industry"]
        if len(type) != 0 and industry_types.count(type) == 0:
            industry_types.append(type)
    return industry_types


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    salaries_list = []
    jobs_list = read(path)
    for job in jobs_list:
        salary = job["max_salary"]
        if salary.isnumeric():
            int_salary = int(salary)
            salaries_list.append(int_salary)
            salaries_list.sort()
    return salaries_list[-1]


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    salaries_list = []
    jobs_list = read(path)
    for job in jobs_list:
        salary = job["min_salary"]
        if salary.isdigit():
            int_salary = int(salary)
            salaries_list.append(int_salary)
            salaries_list.sort()
    return salaries_list[0]


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
