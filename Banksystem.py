from functools import wraps

# 1. გლობალური ცვლადები
SYSTEM_ACTIVE = True
GLOBAL_AUDIT_LOG = []

# 2. დეკორატორი
def audit_system(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: შეამოწმეთ SYSTEM_ACTIVE და ჩაწერეთ GLOBAL_AUDIT_LOG-ში
        global SYSTEM_ACTIVE, GLOBAL_AUDIT_LOG
        if SYSTEM_ACTIVE:
            GLOBAL_AUDIT_LOG.append(f"გამოძახებულია ფუნქცია: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 3. გარე ფუნქცია (Closure & Enclosing)
def create_account_generator(initial_balance):
    balance = initial_balance
    transaction_id = 0
    
    # TODO: შექმენით გენერატორი ფუნქცია, რომელიც იყენებს nonlocal-ს,
    # აახლებს ბალანსს და აბრუნებს (yield) ახალ მდგომარეობას.
    # არ დაგავიწყდეთ დეკორატორის გამოყენება!
    @audit_system
    def account_generator():
        nonlocal balance, transaction_id
        while True:
            # yield აბრუნებს ტრანზაქციის ID-ს და მიმდინარე ბალანსს, 
            # ხოლო .send()-ით იღებს ახალ თანხას (მოლაპარაკებისამებრ)
            amount = yield (transaction_id, balance)
            if amount is not None:
                transaction_id += 1
                balance += amount
                
    return account_generator()