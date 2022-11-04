from hstest import PlottingTest, WrongAnswer, dynamic_test, TestedProgram, CheckResult

dict_img1_data_CORRECT = {
    "pie_data": [['Other countries', 343], ['USA', 237], ['Germany', 98], ['UK', 91], ['France', 43],
                 ['Russia', 32], ['Austria', 26], ['Canada', 26], ['Poland', 25]]}


class Pie(PlottingTest):

    @dynamic_test
    def test(self):
        pr = TestedProgram()
        output = pr.start().replace(" ", "").lower()
        all_figures = self.all_figures()
        if len(all_figures) == 0:
            raise WrongAnswer("Looks like you didn't present any plots")
        if len(all_figures) != 1:
            raise WrongAnswer(f"Expected 1 image of Nobel laureates countries distribution")
        graph1_type = all_figures[0].type

        if graph1_type != "pie":
            raise WrongAnswer("The type of the first plot is wrong. The bar plot is expected.")

        graph1_data = all_figures[0].data.tolist()
        if not graph1_data == dict_img1_data_CORRECT["pie_data"]:
            raise WrongAnswer("Wrong data on the plot. Check data labels and data values.")
        return CheckResult.correct()


if __name__ == '__main__':
    Pie().run_tests()