var { composeAPI } = require('@iota/core')

const IOTA = require('iota.lib.js')
const iota = new IOTA({ provider: 'http://localhost:14265'})

const trytes =
	  'HELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDD'
const message = iota.utils.toTrytes('Hello World!')

const transfers = [{
	value: 0,
	address: trytes,
}]

console.log(process.argv)
async function sendMultipleTransaction(amount) {
	for (let i = 0; i < amount; i = i + 1) {		
		await iota.api.sendTransfer(
			trytes, 3, 14,
			[{
					...transfers[0],
				messsage: `bench marking ${i}`,
			}], (error, success) => {
				if (error) {
					console.log(error)
				}
			}
		)
	}
}
sendMultipleTransaction(process.argv[2])
