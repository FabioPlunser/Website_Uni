<script lang="ts">
	// Input Variables
	export let values: boolean[];
	export let input_names: String[];
	export let show_position: boolean = false;

	// Output Variables
	export let packets: boolean[][] = [];

	let num_inputs: number;
	$: num_inputs = input_names.length;
	let kv_size: [x: number, y: number];
	$: kv_size = [1 << ((num_inputs + 1) >> 1), 1 << (num_inputs >> 1)];

	// Map all Minterms to their corresponding KV-Map Index
	let number_minterms: number[];
	$: number_minterms = values.filter((x) => x).map((_, i) => i);

	let simplified_packets: number[][];
	$: {
		simplified_packets = number_minterms.map((x) => [x]);
		let packets_found: number = number_minterms.length;
		let packets_old: number[][] = [];
		let temp_packets: number[][] = number_minterms.map((x) => [x]);

		while (packets_found >= 1) {
			packets_found = 0;
			simplified_packets.concat(temp_packets);
			packets_old = temp_packets;
			temp_packets = [];
			for (let i = 0; i < packets_old.length; i++) {
				packet_loop: for (let j = i + 1; j < packets_old.length; j++) {
					let difference = packets_old[j][0] - packets_old[i][0];
					// Check if only one Bit is flipped
					if (
						check_if_bit_flipped(
							packets_old[j][0],
							packets_old[i][0]
						)
					) {
						if (
							!check_for_duplicate(packets_old[j], packets_old[i])
						) {
							for (let l = 0; l < packets_old[i].length; l++) {
								if (
									packets_old[j][l] - packets_old[i][l] !=
									difference
								) {
									continue packet_loop;
								}
							}
							simplified_packets.push(
								packets_old[i].concat(packets_old[j])
							);
							packets_found++;
						}
					}
				}
			}
		}

		simplified_packets = simplified_packets.concat(temp_packets);

		// Remove unneccessary Packets

		let needed_packets: number[] = number_minterms;
		let all_minterms: number[] = [];
		for (let i = 0; i < simplified_packets.length; i++) {
			// Create Packet Array with recorded Values
			for (let j = 0; j < simplified_packets[i].length; j++) {
				all_minterms.push(simplified_packets[i][j]);
			}
		}

		let j = 0;
		let temp: number[];
		for (let i = 0; i < simplified_packets.length; i++) {
			// Remove one Packet to check if it is neccessary
			temp = all_minterms.splice(j, simplified_packets[i].length);

			// Check if all Cells are still covered
			if (check_for_missing(all_minterms, needed_packets)) {
				// Remove unneccessary Packet
				simplified_packets.splice(i, 1);
				i--;
			} else {
				// Readd Packet because it is neccessary
				all_minterms.splice(j, 0, ...temp);
				j += simplified_packets[i].length;
			}
		}
	}
	function check_if_bit_flipped(number_one: number, number_two: number) {
		// Get a number containing all Bits that appear in exactly one of the numbers
		let different_bits = number_one ^ number_two;
		// If only one Bit is set in the new number then it is 2^(Position of the Bit)
		return isPowerOfTwo(different_bits);
	}
	function isPowerOfTwo(n: number): boolean {
		return n != 0 && (n & (n - 1)) == 0;
	}
	// Check if array1 and array2 have a duplicate Value
	function check_for_duplicate<a>(array1: a[], array2: a[]) {
		let i, j;
		let found = 0;

		for (j = 0; j < array2.length; j++) {
			for (i = 0; i < array1.length; i++) {
				if (array1[i] == array2[j]) {
					return true;
				}
			}
		}

		return false;
	}
	// Check if array2 is contained in array1
	function check_for_missing(array1: number[], array2: number[]) {
		var i, j;
		var found = 0;

		for (j = 0; j < array2.length; j++) {
			for (i = 0; i < array1.length; i++) {
				if (array1[i] == array2[j]) {
					found++;
					// Break on the first Match
					break;
				}
			}
		}

		return found == array2.length;
	}
</script>

<table class="table-fixed border-seperate">
	<tr>
		<td>Test</td>
	</tr>
</table>
