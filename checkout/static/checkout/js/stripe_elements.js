/* Logic for payment found at : https://stripe.com/docs/payments/accept-a-payment */
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#201f25',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#201f25'
        }
    },
    invalid: {
        color: '#c41324',
        iconColor: '#c41324'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handles validation errors on the card element
card.addEventListener('change', function(event){
    var error = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fa fa-exclamation-triangle"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(error).html(html);
    } else{
        error.textContent = '';
    }
});

// Handle payment form submission
// Code taken from Stripe documentation with some changes to suit our needs
var form = document.getElementById('pay-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-form-button').attr('disabled', true);
    $('#pay-form').fadeToggle(100);
    $('#loading-payment-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var error = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(error).html(html);
            $('#pay-form').fadeToggle(100);
            $('#loading-payment-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});