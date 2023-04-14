from inspect import isfunction

from hstest import PlottingTest, WrongAnswer, dynamic_test, TestedProgram, CheckResult

dict_data_CORRECT = {
    "countries": ['other countries', 'usa', 'germany', 'uk', 'france', 'russia', 'austria', 'canada', 'poland'],
    "count": [343, 237, 98, 91, 43, 32, 26, 26, 25],
    "colors": ['blue', 'orange', 'red', 'yellow', 'green', 'pink', 'brown', 'cyan', 'purple'],
    "autopct": "fsdf",
    "counterclock": True,
    "explode": [0, 0, 0, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08],
}


class Pie(PlottingTest):

    @dynamic_test
    def test(self):
        pr = TestedProgram()
        pr.start()
        all_figures = self.all_figures()
        if len(all_figures) == 0:
            raise WrongAnswer("Looks like you didn't present any plots")
        if len(all_figures) != 1:
            raise WrongAnswer(f"Expected one pie plot of Nobel laureates countries distribution, "
                              f"found {len(all_figures)} plots.")
        graph_type = all_figures[0].type

        if graph_type != "pie":
            raise WrongAnswer(f"The type of the first plot is wrong.\n"
                              f"The pie plot is expected, found {graph_type} plot.")

        graph_data_countries = all_figures[0].data.x.tolist()

        try:
            graph_data_countries = [x.lower() for x in graph_data_countries]
        except:
            raise WrongAnswer("Didn't find names of the countries in the plot.")

        graph_data_count = all_figures[0].data.y.tolist()

        if "other countries" not in graph_data_countries:
            raise WrongAnswer("Didn't find \"Other countries\" category in the pie plot.\n"
                              "Please refer to the objective #1 in the stage description.")
        if not set(graph_data_countries) == set(dict_data_CORRECT["countries"]):
            raise WrongAnswer(f"The list of the countries presented in the pie plot is wrong.\n"
                              f"Expected:\n{dict_data_CORRECT['countries']}\n"
                              f"Found: \n{graph_data_countries}")

        if not set(graph_data_count) == set(dict_data_CORRECT["count"]):
            raise WrongAnswer("Distribution of countries displayed in the pie plot is wrong")

        if not all_figures[0].kwargs.get("colors"):
            raise WrongAnswer("Please define 'colors' parameter!")
        elif not set(all_figures[0].kwargs.get("colors")) == set(dict_data_CORRECT["colors"]):
            raise WrongAnswer("The 'colors' in the pie plot are wrong!")

        if not all_figures[0].kwargs.get("autopct"):
            raise WrongAnswer("The 'autopct' parameter is not defined!")
        elif not isfunction(all_figures[0].kwargs.get("autopct")):
            raise WrongAnswer("The 'autopct' parameter is not a function!")

        if not all_figures[0].kwargs.get("explode"):
            raise WrongAnswer("Please define 'explode' parameter!")
        elif not set(all_figures[0].kwargs.get("explode")) == set(dict_data_CORRECT["explode"]):
            raise WrongAnswer("The 'explode' values in the pie plot are wrong!")

        return CheckResult.correct()


if __name__ == '__main__':
    Pie().run_tests()
