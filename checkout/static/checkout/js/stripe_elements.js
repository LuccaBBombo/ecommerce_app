/* Logic for payment found at : https://stripe.com/docs/payments/accept-a-payment */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
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