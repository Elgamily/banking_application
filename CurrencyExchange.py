from FileManager import FileManager
from HistoryMessages import HistoryMessages

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict, self.hist_file_path)

        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json
    
        # self.file_manager 

    def get_exchange_rates(self):
        url = "https://fake-api.apps.berlintech.ai/api/currency_exchange"
        response = requests.get(url)
        
        resulting_dictionary = json.loads(response.text)

        return resulting_dictionary
    
        # Implement a process that sends a get request to the link 
        # and returns the resulting dictionary.
    
    def exchange_currency(self, currency_from, currency_to, amount):
        try:
            if float(amount) > 0:
                resulting_dictionary = self.get_exchange_rates()

                exchange_failed = True

                if currency_from in resulting_dictionary and currency_to in resulting_dictionary:
                    converted_amount = float(amount) * resulting_dictionary[currency_to] / resulting_dictionary[currency_from]
                    exchange_failed = False

                if exchange_failed == True:
                    print("Currency exchange failed!")

                    history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
                else:
                    history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)

                    self.write_to_history(history_message)
                    
                    return converted_amount
            else:
                print("Currency exchange failed!")

                history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
        except Exception as e:
            print("Currency exchange failed!")

            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)

        self.write_to_history(history_message)

        # implement a process that transfers the specified amount from currency `currency_from` 
        # to currency `currency_to` and, if positive, returns the amount in the new currency

        # with a positive outcome, the record of history looks like this 
        # history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
        # self.write_to_history(history_message)
        
        # in case of a negative outcome, the history entry looks like this
        # - if currency_from or currency_to is specified incorrectly
        # - if amount is not a number
        # history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
        # self.write_to_history(history_message)