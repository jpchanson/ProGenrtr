

class ProjectTypesList:
    def __init__(self, projectType, config=None):
            self.config_ = config;

    def run(self):
        print("Listing project types contained in: '" + self.config_ + "'");


