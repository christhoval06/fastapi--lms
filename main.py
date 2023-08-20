import uvicorn

if __name__ == "__main__":
    uvicorn.run("lms.main:app", host="0.0.0.0", port=8000, reload=True)


# https://github.com/mongodb-developer/FARM-Auth/tree/master