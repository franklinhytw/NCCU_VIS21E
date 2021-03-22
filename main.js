const fs = require('fs');

const rawdata = fs.readFileSync('tmp.json');
let data = JSON.parse(rawdata);

let process_data = [];

for( d of data) {
    let obj = {'year': d.year, values: []};

    var c_list = ['dead', 'A1-hurt', 'A2-hurt'];

    for(var i = 0 ; i < 3 ; i++) {
        let val = {'value': d[c_list[i]], 'class': c_list[i]};
        obj.values.push(val);
    }
    process_data.push(obj);
}

console.log(JSON.stringify(process_data));