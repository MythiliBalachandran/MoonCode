let filename = '/Users/91949/Downloads/temperature_reading - temperature_reading.csv';

d3.csv(filename).then(function(loadedData) {
   let data = [];
   let labels = [];
   let arr = [];

   for (let i = 0; i < loadedData.length; i++) {
      let Timex = loadedData[i].Time;
      labels.push(Timex);

      let Temperature = loadedData[i].temp;
      data.push(Temperature);

      let Set_Value = loadedData[i].Set;
      arr.push(Set_Value/100);
   }

   new Chart(document.getElementById("linechart"), {
      type: 'line',
      data: {
         labels: labels,
         datasets: [
            {
               data: data,
               label: "Temperature curve",
               borderColor: "#3cba9f",
               fill: false
            },
            {
               data: arr,
               label: "Set value",
               borderColor: "rgb(255, 0, 0)",
               fill: false
            }
         ]
      },
      options: {
         title: {
            display: true,
            //text: 'Chart JS Line Chart Example'
         }
      }
   });
});
