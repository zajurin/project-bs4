# import phonenumbers
# from phonenumbers import carrier, timezone, geocoder



# my_number = phonenumbers.parse("+447986123456", "GB")

# print(phonenumbers.is_valid_number(my_number))
# print(carrier.name_for_number(my_number, "en"))
# print(timezone.time_zones_for_number(my_number))
# print(geocoder.description_for_number(my_number, 'en'))

# import phonenumbers

# text_block = "Our services will cost about 2,200 USD and we will deliver the product by the 10.10.2021. For more information, you can call us at +44 7986 123456 or send an e-mail to demo@example.com"

# for match in phonenumbers.PhoneNumberMatcher(text_block, "GB"):
#     print(match)


# import phonenumbers

# text_block = "Our services will cost about 2,200 USD and we will deliver the product by the 10.10.2021. For more information you can call us at +44-7986-123456 or 020 8366 1177 send an e-mail to demo@example.com"

# for match in phonenumbers.PhoneNumberMatcher(text_block, "GB"):
#     print(match)

# import phonenumbers
# formatter = phonenumbers.AsYouTypeFormatter("TR")

# import phonenumbers
# from phonenumbers import geocoder

# my_number = phonenumbers.parse("+447986123456")
# print(geocoder.description_for_number(my_number, "en"))

# import phonenumbers
# from phonenumbers import carrier

# my_number = phonenumbers.parse("+40721234567")
# print(carrier.name_for_number(my_number, "en"))

import phonenumbers
from phonenumbers import timezone

my_number = phonenumbers.parse("+523317904040")
print(timezone.time_zones_for_number(my_number))