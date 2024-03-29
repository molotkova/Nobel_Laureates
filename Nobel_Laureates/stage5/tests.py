from hstest import PlottingTest, WrongAnswer, dynamic_test, TestedProgram, CheckResult

dict_img1_data_CORRECT = {
    "male_yaxis": [194, 69, 107, 78, 218, 198],
    "female_yaxis": [4, 1, 15, 14, 4, 13],
    "label_male": "Males",
    "label_female": "Females",
    "color_male": "blue",
    "color_female": "crimson",
    "width": 0.4,
}


class Bar(PlottingTest):

    @dynamic_test
    def test(self):
        pr = TestedProgram()
        pr.start()

        all_figures = self.all_figures()
        if len(all_figures) == 0:
            raise WrongAnswer("Looks like you didn't present any plots")
        if len(all_figures) != 2:
            raise WrongAnswer(f"Expected one image of gender distribution across Nobel prize categories")
        graph1_type, graph2_type = all_figures[0].type, all_figures[1].type

        if graph1_type != "bar" or graph2_type != "bar":
            raise WrongAnswer("The type of the graph is wrong. The bar plot is expected.")

        graph1_data_x, graph1_data_y = all_figures[0].data.x.tolist(), all_figures[0].data.y.tolist()
        graph2_data_x, graph2_data_y = all_figures[1].data.x.tolist(), all_figures[1].data.y.tolist()

        if not set(graph1_data_y) == set(dict_img1_data_CORRECT["male_yaxis"]):
            raise WrongAnswer(
                "Wrong y-axis data. The values for male Nobel laureates are wrong!")

        if not set(graph2_data_y) == set(dict_img1_data_CORRECT["female_yaxis"]):
            raise WrongAnswer(
                "Wrong y-axis data. The values for female Nobel laureates are wrong!")

        if not all_figures[0].kwargs.get("label"):
            raise WrongAnswer("Please define 'label' parameter for the 'Males'!")
        elif not all_figures[0].kwargs.get("label") == dict_img1_data_CORRECT["label_male"]:
            raise WrongAnswer(f"The 'label' for the 'Males' is wrong. Make sure it is used for the first group!")

        if not all_figures[1].kwargs.get("label"):
            raise WrongAnswer("Please define 'label' parameter for the 'Females'!")
        elif not all_figures[1].kwargs.get("label") == dict_img1_data_CORRECT["label_female"]:
            raise WrongAnswer(f"The 'label' for the 'Females' is wrong. Make sure it is used for the second group!")

        if not all_figures[0].kwargs.get("color"):
            raise WrongAnswer("Please define 'color' parameter for the 'Males'!")
        elif not all_figures[0].kwargs.get("color") == dict_img1_data_CORRECT["color_male"]:
            raise WrongAnswer(f"The 'color' for the 'Males' should be '{dict_img1_data_CORRECT['color_male']}'!")

        if not all_figures[1].kwargs.get("color"):
            raise WrongAnswer("Please define 'color' parameter for the 'Females'!")
        elif not all_figures[1].kwargs.get("color") == dict_img1_data_CORRECT["color_female"]:
            raise WrongAnswer(f"The 'color' for the 'Females' should be '{dict_img1_data_CORRECT['color_female']}'!")

        if not all_figures[0].kwargs.get("width"):
            raise WrongAnswer("Please define 'width' parameter for the 'Males'!")
        elif not all_figures[0].kwargs.get("width") == dict_img1_data_CORRECT["width"]:
            raise WrongAnswer(f"The 'width' for the 'Males' should be '{dict_img1_data_CORRECT['width']}'!")

        if not all_figures[1].kwargs.get("width"):
            raise WrongAnswer("Please define 'width' parameter for the 'Females'!")
        elif not all_figures[1].kwargs.get("width") == dict_img1_data_CORRECT["width"]:
            raise WrongAnswer(f"The 'width' for the 'Females' should be '{dict_img1_data_CORRECT['width']}'!")

        return CheckResult.correct()


if __name__ == '__main__':
    Bar().run_tests()
