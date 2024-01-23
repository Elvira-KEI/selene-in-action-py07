from pathlib import Path

from selene.support.shared import browser
from selene import have



def test_demoqa_registration_form(browser_settings):

   browser.open('/automation-practice-form')

   browser.element('#firstName').type('Elvira')
   browser.element('#lastName').type('Kondrateva')
   browser.element('#userEmail').type('elvira.mnacakanian@gmail.com')
   browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
   browser.element('#userNumber').type('8902488980')

   browser.element('#dateOfBirthInput').click()
   browser.element('.react-datepicker__month-select').send_keys('December')
   browser.element('.react-datepicker__year-select').send_keys('1989')
   browser.element('.react-datepicker__day--028:not(.react-datepicker__day--outside-month)').click()

   browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()

   browser.element('#uploadPicture').set_value(str(Path(__file__).absolute().parent.joinpath('resources', 'IMG_20220927_180119.jpg')))

   browser.element('#currentAddress').type('Baker st. 221B')

   browser.element('#submit').click()

   browser.element('[id=example-modal-sizes-title-lg]').should(
       have.text('Thanks for submitting the form')
   )

   browser.element('.table').all('td').even.should(
      have.texts( 'Elvira Kondrateva',
                  'elvira.mnacakanian@gmail.com',
                  'Female',
                  '8902488980',
                  '28 December,1989',
                  '',
                  'Sports',
                  'IMG_20220927_180119.jpg',
                  'Baker st. 221B',
                  '',))