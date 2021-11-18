/* globals Chart:false, feather:false */
let labels = [];
  axios.get('http://localhost:5000/week').then(({data}) =>
          data.forEach(function(item,i) {
            newd =new Date(item.date).toLocaleDateString();
            labels.push(newd)

        })
      
      ).catch((err) => console.log(err))
      

  'use strict'
  console.log(labels)
  let data = [];
  axios.get('http://localhost:5000/value').then((res) =>
            res.data.forEach(function(item,i) {
            console.log(item.counted_leads)
            data.push(item.counted_leads)

        })
      ).catch((err) => console.log(err))
      console.log(data);

  feather.replace({ 'aria-hidden': 'true' })

  

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        data,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

