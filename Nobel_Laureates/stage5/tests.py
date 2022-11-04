from hstest import PlottingTest, WrongAnswer, dynamic_test, TestedProgram, CheckResult

dict_img1_data_CORRECT = {
    "male_yaxis": [194, 69, 107, 78, 218, 198],
    "female_yaxis": [4, 1, 15, 14, 4, 13]}


class Bar(PlottingTest):

    @dynamic_test
    def test(self):
        pr = TestedProgram()
        output = pr.start().replace(" ", "").lower()

        all_figures = self.all_figures()
        if len(all_figures) == 0:
            raise WrongAnswer("Looks like you didn't present any plots")
        if len(all_figures) != 2:
            raise WrongAnswer(f"Expected 1 image of gender distribution across Nobel prize categories")
        graph1_type, graph2_type = all_figures[0].type, all_figures[1].type

        if graph1_type != "bar" or graph2_type != "bar":
            raise WrongAnswer("The type of the first plot is wrong. The bar plot is expected.")

        graph1_data_x, graph1_data_y = all_figures[0].data.x.tolist(), all_figures[0].data.y.tolist()
        graph2_data_x, graph2_data_y = all_figures[1].data.x.tolist(), all_figures[1].data.y.tolist()

        if not ((graph1_data_y == dict_img1_data_CORRECT["male_yaxis"] and
                 graph2_data_y == dict_img1_data_CORRECT["female_yaxis"])
                or (graph1_data_y == dict_img1_data_CORRECT["female_yaxis"] and graph2_data_y ==
                    dict_img1_data_CORRECT["male_yaxis"])):
            raise WrongAnswer("Wrong y-axis data on the first plot.\n"
                              "The number of female and male Nobel laureates in each category is expected.")

        return CheckResult.correct()


if __name__ == '__main__':
    Bar().run_tests()