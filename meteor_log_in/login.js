if (Meteor.isClient) {
    // counter starts at 0
    Session.setDefault('counter', 0);

    Template.hello.helpers({
        counter: function () {
            return Session.get('counter');
        }
    });

    Template.hello.events({
        'click button': function () {
            // increment the counter when button is clicked
            Session.set('counter', Session.get('counter') + 1);
        }
    });

    Template.login.events({
        'submit #login-form': function (e, t) {
            e.preventDefault();
            // retrieve the input field values
            var email = t.find('#login-email').value
                , password = t.find('#login-password').value;

            // TODO Trim and validate your fields here...
            // If validation passes, supply the appropriate fields to the
            // Meteor.loginWithPassword() function.

            Meteor.loginWithPassword(email, password, function (err) {
                if (err) {
                    // The user might not have been found, or their password
                    // could be incorrect. Inform the user that their
                    // login attempt has failed.
                }
                else {
                    console.log("The user has been logged in.")
                    // The user has been logged in.
                }
            });
            return false;
        }
    });

    Template.register.events({
        'submit #register-form': function (e, t) {
            e.preventDefault();
            var email = t.find('#account-email').value
                , password = t.find('#account-password').value;

            // Trim and validate the input

            Accounts.createUser({email: email, password: password}, function (err) {
                if (err) {
                    //
                } else {
                    console.log("Account was created")
                    //Success
                }
            });
            return false;
        }
    });


}

if (Meteor.isServer) {
    Meteor.startup(function () {
        // code to run on server at startup
    });
}
