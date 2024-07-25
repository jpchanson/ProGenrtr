

class ProjectGenerator:
    def __init__(self, projectType, config=None):
        self.projectType_ = projectType;
        if config == None:
            self.config_ = "~/.Progenrtr.conf";
        else:
            self.config_ = config;

    def run(self):
        print("Project Type: " + self.projectType_)
        print("config: " + self.config_)

