# sending-email
This action sends notification email to a specified person. 

## Inputs

### `destination-email`

**Required** The name of the person to greet. Default `"example@gmail.com"`.

## Example usage

uses: nguyennv19/sending-email
with:
destination-email: 'example@gmail.com'

## Environment
### `USER_EMAIL`
The email used to send out notification.
### `USER_PASSWORD`
Email password.