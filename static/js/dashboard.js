/* globals Chart:false, feather:false */

      
(function () {
  'use strict'

  let labels = [];
  axios.get('http://localhost:5000/week').then(({data}) =>
          data.forEach(function(item,i) {
            newd =new Date(item.date).toLocaleDateString();
            labels.push(newd)

        })
      
      ).catch((err) => console.log(err))
      console.log(labels)
  feather.replace({ 'aria-hidden': 'true' })

  

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ],
      datasets: [{
        data: [
          15339,
          21345,
          18483,
          24003,
          23489,
          24092,
          12034
        ],
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
})()
