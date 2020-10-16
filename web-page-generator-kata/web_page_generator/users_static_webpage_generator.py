class UsersStaticWebPageGenerator:
    def generate_file(self, users):

        # save resulting static html page
        file = open("html/users.html", "w")

        file.write("<!doctype html>\n")
        file.write("<html lang=\"en\">\n")
        file.write("<head>\n")
        file.write("<meta charset=\"utf-8\">\n")
        file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n")

        file.write("<title>User biographies</title>\n")

        file.write("<!-- Bootstrap core CSS -->\n")
        file.write("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css\" integrity=\"sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4\" crossorigin=\"anonymous\">\n")

        file.write("<!-- Custom styles for this template -->\n")
        file.write("<link href=\"assets/cover.css\" rel=\"stylesheet\">\n")
        file.write("</head>\n")

        file.write("<body class=\"text-center\">\n")

        file.write("<div class=\"cover-container d-flex w-100 h-100 p-3 mx-auto flex-column\">\n")
        file.write("<header class=\"masthead mb-auto\">\n")
        file.write("<div class=\"inner\">\n")
        file.write("<h3 class=\"masthead-brand\">Users Biography</h3>\n")
        file.write("<nav class=\"nav nav-masthead justify-content-center\">\n")
        file.write("<a class=\"nav-link active\" href=\"#\">Home</a>\n")
        file.write("<a class=\"nav-link\" href=\"#\">Features</a>\n")
        file.write("<a class=\"nav-link\" href=\"#\">Contact</a>\n")
        file.write("</nav>\n")
        file.write("</div>\n")
        file.write("</header>\n")

        file.write("<main role=\"main\" class=\"inner cover\">\n")
        for user in users:
            file.write("<h1 class=\"cover-heading\">" + user.name + "</h1>\n")
            self.add_labels(file, user)
            file.write("<p class=\"lead\">" + user.biography + "</p>\n")
        file.write("</main>\n")

        file.write("<footer class=\"mastfoot mt-auto\">\n")
        file.write("<div class=\"inner\">\n")
        file.write(
            "<p>Sprout class kata created by Codium <a href=\"https://twitter.com/CodiumTeam\">@CodiumTeam</a>. Cover template for <a href=\"https://getbootstrap.com/\">Bootstrap</a>, by <a href=\"https://twitter.com/mdo\">@mdo</a>.</p>\n")
        file.write("</div>\n")
        file.write("</footer>\n")
        file.write("</div>\n")

        file.write("<!-- Bootstrap core JavaScript\n")
        file.write("        ================================================== -->\n")
        file.write("<!-- Placed at the end of the document so the pages load faster -->\n")
        file.write(
            "<script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>\n")
        file.write(
            "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js\" integrity=\"sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ\" crossorigin=\"anonymous\"></script>\n")
        file.write(
            "<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js\" integrity=\"sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm\" crossorigin=\"anonymous\"></script>\n")
        file.write("</body>\n")
        file.write("</html>\n")

    def add_labels(self, file, user):
        self.add_score_label(file, user)
        self.add_localization_label(file, user)
        self.add_community_manager_label(file, user)

    def add_score_label(self, file, user):
        points = 0
        for keywords in ['edición', 'sociedad', 'mundo', 'libro', 'texto', 'revista', 'valores', 'educación', 'teatro', 'social']:
            if self.is_in_biography(user, keywords):
                points += 1
        file.write('<button type="button" class="btn btn-warning">Score <span class="badge badge-light">' + str(points) + '</span><span class="sr-only">keywords found</span></button>')


    def add_localization_label(self, file, user):
        for city in ['Barcelona', 'Madrid', 'Granada', 'Vigo', 'Palma de Mallorca']:
            if (self.is_in_biography(user, city)):
                file.write('<span class="badge badge-pill badge-info">' + city+'</span>')

        pass

    def add_community_manager_label(self, file, user):
        if (self.is_in_biography(user, 'community manager')):
            file.write('<span class="badge badge-pill badge-danger">Community manager</span>')

    @staticmethod
    def is_in_biography(user, word):
        return word.lower() in user.biography.lower()
