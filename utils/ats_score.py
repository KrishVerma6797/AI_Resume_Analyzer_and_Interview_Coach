def skill_score(skills):
    if len(skills)<5:
        return 10
    elif len(skills)<10:
        return 25
    else:
        return 40
    
def project_score(text):
    for t in text.lower().split():
        if t in ["project","developed","projects","built","implemented"]:
            return 30
    return 0

def edu(text):
    for t in text.lower().split():
        if t in ['be','b.e.','btech','b.tech','bachelors','bachelor','university','college']:
            return 20
    return 0

def  certificate(text):
    for t in text.lower().split():
        if t in ['certificate','certificates','coursera','udemy','nptel']:
            return 10
    return 0

def keyword_match(jd_skills,skills):
    resume=set([s.lower() for s in skills])
    jd=set([s.lower() for s in jd_skills])
    matched=len(resume.intersection(jd))
    total=len(jd)
    return (matched/total)*100 if total>0 else 0
def ats_score(skills,text):
    skill=skill_score(skills)
    project=project_score(text)
    education=edu(text)
    cert=certificate(text)
    return skill+project+education+cert
def missing_skills(jd_skills,skills):
    resume=set([s.lower() for s in skills])
    jd=set([s.lower() for s in jd_skills])
    missing=jd.difference(resume)
    return list(missing)

def suggestions(skills,text):
    suggestions = []
    if "docker" not in skills:
        suggestions.append("Learn Docker")

    if "git" not in skills:
        suggestions.append("Add Git/GitHub skills")

    if len(skills) < 5:
        suggestions.append("Add more technical skills")

    return suggestions