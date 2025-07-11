import unittest
import pandas as pd
from demographic_data_analyzer import calculate_demographic_data

class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_calculate_demographic_data(self):
        result = calculate_demographic_data(print_data=False)

        self.assertEqual(result['average_age_men'], 39.4)
        self.assertEqual(result['percentage_bachelors'], 16.4)
        self.assertEqual(result['higher_education_rich'], 46.5)
        self.assertEqual(result['lower_education_rich'], 17.4)
        self.assertEqual(result['min_work_hours'], 1)
        self.assertEqual(result['rich_percentage'], 10.0)
        self.assertEqual(result['highest_earning_country'], 'Iran')
        self.assertEqual(result['highest_earning_country_percentage'], 41.9)
        self.assertEqual(result['top_IN_occupation'], 'Prof-specialty')

        expected_race_count = pd.Series(
            data=[23393, 2824, 1039, 311, 271],
            index=['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
        )
        pd.testing.assert_series_equal(result['race_count'], expected_race_count)

if __name__ == "__main__":
    unittest.main()
