from MobilePhoneMastsAnalysis.process_phone_masts_file import ProcessMobilePhoneMasts


class MockedDataProcessMobilePhoneMasts(ProcessMobilePhoneMasts):
    def get_data_from_file(self):
        return [
            {
                'Current Rent': '9500.00',
                'Lease Years': '25',
                'Tenant Name': 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd',
                'Lease Start Date': '01 Aug 2009',
            },
            {
                'Current Rent': '20000.00',
                'Lease Years': '12',
                'Tenant Name': 'Everything Everywhere Ltd',
                'Lease Start Date': '24 Jun 1999',
            },
            {
                'Current Rent': '6600.00',
                'Lease Years': '25',
                'Tenant Name': 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd',
                'Lease Start Date': '07 Oct 2004',
            },
            {
                'Current Rent': '12250.00',
                'Lease Years': '15',
                'Tenant Name': 'Everything Everywhere Ltd',
                'Lease Start Date': '01 Dec 2001',
            },
            {
                'Current Rent': '12750.00',
                'Lease Years': '25',
                'Tenant Name': 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd',
                'Lease Start Date': '27 Feb 1995',
            },
            {
                'Current Rent': '12000.00',
                'Lease Years': '10',
                'Tenant Name': 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd',
                'Lease Start Date': '03 Mar 2008',
            },
        ]


def test_first_solution():
    processor = MockedDataProcessMobilePhoneMasts()
    results = processor.solve_first_task()
    expected_rents = ['6600.00', '9500.00', '12000.00', '12250.00', '12750.00']
    for result, expected_rent in zip(results, expected_rents):
        assert result['Current Rent'] == expected_rent


def test_second_solution():
    processor = MockedDataProcessMobilePhoneMasts()
    filtered_data, total_rent = processor.solve_second_task()
    for result in filtered_data:
        assert result['Lease Years'] == '25'
    assert total_rent == 28850.0


def test_third_solution():
    processor = MockedDataProcessMobilePhoneMasts()
    result = processor.solve_third_task()
    expected = {
        'Hutchinson3G Uk Ltd&Everything Everywhere Ltd': 4,
        'Everything Everywhere Ltd': 2
    }
    assert result == expected


def test_fourth_solution():
    processor = MockedDataProcessMobilePhoneMasts()
    results = processor.solve_fourth_task()
    expected_data = [
        {
            'Current Rent': '20000.00',
            'Lease Years': '12',
            'Tenant Name': 'Everything Everywhere Ltd',
            'Lease Start Date': '24/06/1999'
        },
        {
            'Current Rent': '6600.00',
            'Lease Years': '25',
            'Tenant Name': 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd',
            'Lease Start Date': '07/10/2004'
        },
        {
            'Current Rent': '12250.00',
            'Lease Years': '15',
            'Tenant Name': 'Everything Everywhere Ltd',
            'Lease Start Date': '01/12/2001'
        }
    ]
    for result, expected in zip(results, expected_data):
        assert result == expected
