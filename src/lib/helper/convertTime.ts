export function convertToDate(time: any){
    let fromDate = time.date; 
    let toDate = time.date;

    let fromDateParts = fromDate.split(".");
    let toDateParts = toDate.split(".");


    let fromTime = time.time.split("-")[0];
    let toTime = time.time.split("-")[1];

    let fromTimeParts = fromTime.split(".");
    let toTimeParts = toTime.split(".");
    
    
    let englishFromDate = fromDateParts[2] + '/' + fromDateParts[1]  + '/' + fromDateParts[0];
    let englishToDate = toDateParts[2] + '/' + toDateParts[1]  + '/' + toDateParts[0];

    let from = new Date(englishFromDate);
    from.setHours(fromTimeParts[0]);
    from.setMinutes(fromTimeParts[1]);
    let to = new Date(englishToDate);
    to.setHours(toTimeParts[0]);
    to.setMinutes(toTimeParts[1]);

    return {from, to};
}