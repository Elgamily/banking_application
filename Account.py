from FileManager import FileManager
from HistoryMessages import HistoryMessages

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict, self.hist_file_path)

        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json
    
        # self.file_manager 

    def deposit(self, amount):
        try:
            if float(amount) > 0:
                self.balance += float(amount)

                history_message = HistoryMessages.deposit("success", amount, self.balance)
            else:
                print("Invalid amount for deposit!")

                history_message = HistoryMessages.deposit("failure", amount, self.balance)
        except Exception as e:
            print("Invalid amount for deposit!")

            history_message = HistoryMessages.deposit("failure", amount, self.balance)
    
        self.write_to_history(history_message)

        # TODO:
        # implement the deposit process with all necessary checks
        # amount must be a integer greater than 0
        
        # in case of a positive outcome, use this construct to write it to a JSON file

        # history_message = HistoryMessages.deposit("success", amount, self.balance)
        # self.write_to_history(history_message)

        # in case of a negative outcome, use this construct to write to the JSON file
            
        # history_message = HistoryMessages.deposit("failure", amount, self.balance)
        # self.write_to_history(history_message)

    def debit(self, amount):
        try:
            if float(amount) > 0 and float(amount) <= self.get_balance():
                self.balance -= float(amount)

                history_message = HistoryMessages.debit("success", amount, self.balance)
            else:
                print("Invalid amount for debit!")

                history_message = HistoryMessages.debit("failure", amount, self.balance)
        except Exception as e:
            print("Invalid amount for debit!")

            history_message = HistoryMessages.debit("failure", amount, self.balance)

        self.write_to_history(history_message)

        # TODO:
        # implement account debits with all necessary checks
        # amount must be a integer greater than 0
        # if amount is greater than the amount in the account (insufficient funds) the operation should not work

        # in case of positive outcome use this construct to write to JSON file

        # history_message = HistoryMessages.debit("success", amount, self.balance)
        # self.write_to_history(history_message)

        # in case of a negative outcome, use this construct to write to a JSON file
        
        # history_message = HistoryMessages.debit("failure", amount, self.balance)
        # self.write_to_history(history_message)

    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        

    def get_history(self):
        list_of_dicts = self.file_manager.read_json(self.hist_file_path)

        for dictionary in list_of_dicts:
            print(self.dict_to_string(dictionary))
            
        # TODO:
        # implement a process that returns transaction history line by line
        # use the dict_to_string method to create a string from a dictionary