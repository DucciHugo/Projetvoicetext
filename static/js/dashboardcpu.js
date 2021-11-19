var data = []
var myChart = null

function cpustats(cpu){
    console.log(cpu)
    'use strict'
    cpures = cpu[8].slice(0,3)

    data.push(cpures)

    feather.replace({ 'aria-hidden': 'true' })
  
    // Graphs
    var ctx = document.getElementById('cpu')
    // eslint-disable-next-line no-unused-vars
    if(myChart==null){
        myChart = new Chart(ctx, {
            type: 'line',
            data: {
              labels: [
                'test',
              ],
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
        
    }
    myChart.config.data.datasets.push([{
        data,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }])
      myChart.update();
  }
