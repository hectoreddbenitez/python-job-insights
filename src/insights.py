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
    chosen_jobs_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            chosen_jobs_by_industry.append(job)
    return chosen_jobs_by_industry


def get_max_salary(path):
    salaries_list = []
    # jobs_list = read(path)
    for job in read(path):
        salary = job["max_salary"]
        if salary.isnumeric():
            salaries_list.append(int(salary))
            salaries_list.sort()
    return salaries_list[-1]


def get_min_salary(path):
    """refatoração, Ó que"""
    jobs_list = read(path)
    salaries_list = [
        int(job["min_salary"])
        for job in jobs_list
        if job["min_salary"].isdigit()
    ]
    """original"""
    """ jobs_list = read(path)
    # for job in jobs_list:
    #     salary = job["min_salary"]
    #     if salary.isdigit():
    #         salaries_list.append(int(salary))"""
    return min(salaries_list)


def matches_salary_range(job, salary):
    """https://docs.python.org/pt-br/3/tutorial/errors.html"""
    try:
        if job["min_salary"] <= int(salary) <= job["max_salary"]:
            return True
        if job["min_salary"] > job["max_salary"]:
            raise ValueError("não é assim não...")
        return False
    except BaseException as err:
        raise err and ValueError


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
