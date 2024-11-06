# item {name:str,description:str,price:float}
items = []
#order {"name":str,"phone_or_email":str,"items":cart,"status":str,"date_time":datetime.now(),"price":get_price(cart)}
available_status = {"1":"wait",
                    "2":"success",
                    "3":"discard"}
orders = []

admins = []
