# encoding: utf-8
import unittest
import re
from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import floatify_latlng

import httpretty

class OpenCageGeocodeTestCase(unittest.TestCase):
    def setUp(self):
        httpretty.enable()


        self.geocoder = OpenCageGeocode('abcde')

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def testUKPostcode(self):
        httpretty.register_uri(httpretty.GET,
            re.compile("http://prototype.opencagedata.com/geocode/v1/json"),
            body='{"total_results":10,"licenses":[{"name":"CC-BY-SA","url":"http://creativecommons.org/licenses/by-sa/3.0/"},{"name":"ODbL","url":"http://opendatacommons.org/licenses/odbl/summary/"}],"status":{"message":"OK","code":200},"thanks":"For using an OpenCage Data API","rate":{"limit":"2500","remaining":2487,"reset":1402185600},"results":[{"annotations":{},"components":{"country_name":"United Kingdom","region":"Islington","locality":"Clerkenwell"},"formatted":"Clerkenwell, Islington, United Kingdom","geometry":{"lat":"51.5221558691","lng":"-0.100838524406"},"bounds":null},{"formatted":"82, Lokku Ltd, Clerkenwell Road, Clerkenwell, London Borough of Islington, London, EC1M 5RF, Greater London, England, United Kingdom, gb","components":{"county":"London","state_district":"Greater London","road":"Clerkenwell Road","country_code":"gb","house_number":"82","country":"United Kingdom","city":"London Borough of Islington","suburb":"Clerkenwell","state":"England","house":"Lokku Ltd","postcode":"EC1M 5RF"},"annotations":{},"bounds":{"northeast":{"lng":"-0.1023889","lat":"51.5226795"},"southwest":{"lat":"51.5225795","lng":"-0.1024889"}},"geometry":{"lat":"51.5226295","lng":"-0.1024389"}},{"components":{"county":"London","state_district":"Greater London","road":"Clerkenwell Road","country_code":"gb","country":"United Kingdom","city":"London Borough of Islington","suburb":"Clerkenwell","state":"England","postcode":"EC1M 6DS"},"annotations":{},"formatted":"Clerkenwell Road, Clerkenwell, London Borough of Islington, London, EC1M 6DS, Greater London, England, United Kingdom, gb","geometry":{"lat":"51.5225346","lng":"-0.1027003"},"bounds":{"northeast":{"lat":"51.5225759","lng":"-0.1020597"},"southwest":{"lat":"51.5225211","lng":"-0.103223"}}},{"formatted":"Clerkenwell Road, Clerkenwell, London Borough of Islington, London, EC1M 6DS, Greater London, England, United Kingdom, gb, Craft Central","annotations":{},"components":{"postcode":"EC1M 6DS","arts_centre":"Craft Central","state":"England","suburb":"Clerkenwell","country":"United Kingdom","city":"London Borough of Islington","country_code":"gb","road":"Clerkenwell Road","state_district":"Greater London","county":"London"},"bounds":{"northeast":{"lat":"51.52246","lng":"-0.1027652"},"southwest":{"lng":"-0.1028652","lat":"51.52236"}},"geometry":{"lng":"-0.1028152","lat":"51.52241"}},{"components":{"county":"London","state_district":"Greater London","restaurant":"Noodle Express","road":"Albemarle Way","country_code":"gb","country":"United Kingdom","city":"London Borough of Islington","suburb":"Clerkenwell","state":"England","postcode":"EC1M 6DS"},"annotations":{},"formatted":"Noodle Express, Albemarle Way, Clerkenwell, London Borough of Islington, London, EC1M 6DS, Greater London, England, United Kingdom, gb","geometry":{"lng":"-0.10255386845056","lat":"51.5228195"},"bounds":{"southwest":{"lng":"-0.102621","lat":"51.5227781"},"northeast":{"lat":"51.5228603","lng":"-0.1024869"}}},{"geometry":{"lat":"51.5229424","lng":"-0.102380530769224"},"bounds":{"northeast":{"lat":"51.5229759","lng":"-0.1023064"},"southwest":{"lng":"-0.1024639","lat":"51.5229046"}},"annotations":{},"components":{"county":"London","state_district":"Greater London","road":"Albemarle Way","country_code":"gb","cafe":"PAR","country":"United Kingdom","city":"London Borough of Islington","suburb":"Clerkenwell","state":"England","postcode":"EC1M 6DS"},"formatted":"PAR, Albemarle Way, Clerkenwell, London Borough of Islington, London, EC1M 6DS, Greater London, England, United Kingdom, gb"},{"formatted":"Workshop Coffee Co., 27, Clerkenwell Road, Clerkenwell, London Borough of Islington, London, EC1M 5RN, Greater London, England, United Kingdom, gb","components":{"county":"London","state_district":"Greater London","road":"Clerkenwell Road","country_code":"gb","house_number":"27","cafe":"Workshop Coffee Co.","country":"United Kingdom","city":"London Borough of Islington","suburb":"Clerkenwell","state":"England","postcode":"EC1M 5RN"},"annotations":{},"bounds":{"southwest":{"lng":"-0.1024422","lat":"51.5222246"},"northeast":{"lng":"-0.1022307","lat":"51.5224408"}},"geometry":{"lat":"51.52234585","lng":"-0.102338899572156"}},{"components":{"county":"London","state_district":"Greater London","road":"St. John Street","country_code":"gb","country":"United Kingdom","city":"London Borough of Islington","suburb":"Clerkenwell","hairdresser":"Franco & Co","state":"England","postcode":"EC1M 6DS"},"annotations":{},"formatted":"St. John Street, Clerkenwell, London Borough of Islington, London, EC1M 6DS, Greater London, England, United Kingdom, gb, Franco & Co","geometry":{"lng":"-0.1024118","lat":"51.5231165"},"bounds":{"southwest":{"lng":"-0.1024618","lat":"51.5230665"},"northeast":{"lng":"-0.1023618","lat":"51.5231665"}}},{"bounds":{"northeast":{"lng":"-0.1023218","lat":"51.5231688"},"southwest":{"lat":"51.5229634","lng":"-0.1024934"}},"geometry":{"lng":"-0.102399365567707","lat":"51.5230257"},"formatted":"St. John Street, Clerkenwell, London Borough of Islington, London, EC1M 6DS, Greater London, England, United Kingdom, gb, MacCarthy","annotations":{},"components":{"county":"London","state_district":"Greater London","road":"St. John Street","country_code":"gb","country":"United Kingdom","city":"London Borough of Islington","suburb":"Clerkenwell","hairdresser":"MacCarthy","state":"England","postcode":"EC1M 6DS"}},{"geometry":{"lng":"-0.102730855172415","lat":"51.52267345"},"bounds":{"northeast":{"lng":"-0.1025498","lat":"51.5227315"},"southwest":{"lat":"51.5226068","lng":"-0.1028931"}},"annotations":{},"components":{"county":"London","state_district":"Greater London","road":"Albemarle Way","country_code":"gb","house_number":"84","country":"United Kingdom","city":"London Borough of Islington","suburb":"Clerkenwell","state":"England","house":"The Printworks","postcode":"EC1M 6DS"},"formatted":"84, The Printworks, Albemarle Way, Clerkenwell, London Borough of Islington, London, EC1M 6DS, Greater London, England, United Kingdom, gb"}],"timestamp":{"created_unix":1402133768,"created_http":"Sat, 07 Jun 2014 09:36:08 GMT"},"we_are_hiring":"http://lokku.com/#jobs"}',
        )

        results = self.geocoder.geocode("EC1M 5RF")
        self.assertTrue(
            any((abs(result['geometry']['lat'] - 51.5201666) < 0.05 and abs(result['geometry']['lng'] - -0.0985142) < 0.05) for result in results),
            msg="Bad result"
        )
                               #'

    def testAustralia(self):
        httpretty.register_uri(httpretty.GET,
            re.compile("http://prototype.opencagedata.com/geocode/v1/json"),
            body='{"licenses":[{"url":"http://creativecommons.org/licenses/by-sa/3.0/","name":"CC-BY-SA"},{"url":"http://opendatacommons.org/licenses/odbl/summary/","name":"ODbL"}],"status":{"message":"OK","code":200},"thanks":"For using an OpenCage Data API","results":[{"geometry":{"lng":"149.5886383","lat":"-32.5980702"},"components":{"country_code":"au","state":"New South Wales","country":"Australia","town":"Mudgee"},"formatted":"Mudgee, New South Wales, Australia, au","annotations":{},"bounds":{"southwest":{"lng":"149.5486383","lat":"-32.6380702"},"northeast":{"lng":"149.6286383","lat":"-32.5580702"}}},{"formatted":"Mudgee, Mid-Western Regional, New South Wales, Australia","components":{"state":"New South Wales","country":"Australia","county":"Mid-Western Regional","town":"Mudgee"},"bounds":{"southwest":{"lng":"149.573196411","lat":"-32.6093025208"},"northeast":{"lng":"149.602890015","lat":"-32.5818252563"}},"annotations":{},"geometry":{"lng":149.5871,"lat":-32.59426}}],"total_results":2,"rate":{"reset":1402185600,"limit":"2500","remaining":2489},"we_are_hiring":"http://lokku.com/#jobs","timestamp":{"created_http":"Sat, 07 Jun 2014 09:31:50 GMT","created_unix":1402133510}}',
        )

        results = self.geocoder.geocode("Mudgee, Australia")
        self.assertTrue(
            any((abs(result['geometry']['lat'] - -32.5980702) < 0.05 and abs(result['geometry']['lng'] - 149.5886383) < 0.05) for result in results),
            msg="Bad result"
        )


#"EC1M 5RF"          => [  51.5201666,  -0.0985142 ],

## Encoding in request
#"Münster"           => [  51.9625101,   7.6251879 ],

## Encoding in response
#"Donostia"          => [   43.300836,  -1.9809529 ],

class FloatifyDictTestCase(unittest.TestCase):
    def _expected_output(input_value, expected_output):
        def test(self):
            self.assertEquals(floatify_latlng(input_value), expected_output)
        return test

    testString = _expected_output("123", "123")
    testEmptyDict = _expected_output({}, {})
    testEmptyList = _expected_output([], [])
    testDictWithFloats = _expected_output({'geom': {'lat': 12.01, 'lng': -0.9}}, {'geom': {'lat': 12.01, 'lng': -0.9}})
    testDictWithStringifiedFloats = _expected_output({'geom': {'lat': "12.01", 'lng': "-0.9"}}, {'geom': {'lat': 12.01, 'lng': -0.9}})
    testDictWithList = _expected_output(
        {'results': [{'geom': {'lat': "12.01", 'lng': "-0.9"}}, {'geometry': {'lat': '0.1', 'lng': '10'}}]},
        {'results': [{'geom': {'lat': 12.01, 'lng': -0.9}}, {'geometry': {'lat': 0.1, 'lng': 10}}]}
    )
    testListWithThings = _expected_output([{'foo': 'bar'}], [{'foo': 'bar'}])
