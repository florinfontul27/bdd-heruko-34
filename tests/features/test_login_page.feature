

    #Given e un fel de before sau preconditii pe care trebuie sa le indeplineasca testul. de ex: load page
    #when = actiuni. de ex: login
    #then = ce verificari facem. de ex: asserturile

    Feature: Test Login Functionality
        Scenario: check login positives testing
        #adica numele testului
            Given : the user open the login page
            When : the user type username
            And : the user type password
            And : the user type log in
            Then : the user is on secure page
            And : the welcome message is displayed
