<?php include 'static/includes/config.php' ?>
<?php include 'static/includes/get.php' ?>


<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <title>Statistiques</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.1/examples/dashboard/">

    

    <!-- Bootstrap core CSS -->
<link href="static/styles/bootstrap.min.css" rel="stylesheet">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>

    
    <!-- Custom styles for this template -->
    <link href="static/styles/dashboard.css" rel="stylesheet">
  </head>
  <body>
    
<header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
  <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">ATHMB</a>
  <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
</header>

<div class="container-fluid">
  <div class="row">
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="position-sticky pt-3">
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link" href="Statistiques.php">
              <span data-feather="home"></span>
              Accueil
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="nbmots.php">
              <span data-feather="book"></span>
              Nombre de mots
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              <span data-feather="bar-chart-2"></span>
              Nombre de conversations
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              <span data-feather="layers"></span>
              Nombre d'actions
            </a>
          </li>
        </ul>

        <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
          <span>Statistiques raspberry</span>
        </h6>
        <ul class="nav flex-column mb-2">
          <li class="nav-item">
            <a class="nav-link" href="#">
              <span data-feather="file-text"></span>
              Taux d’utilisation du CPU
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              <span data-feather="file-text"></span>
              Taux d’utilisation de la RAM
            </a>
          </li>
        </ul>
        <hr>
        <li class="nav-item mb-1 mb-md-0 mx-1">
          <a class="text-white btn btn-danger" href="index.html">
              Retour vers la page d'accueil
          </a>
      </div>
    </nav>

    <main>
                        <div class="row">
                        <div class="col-sm-4 mb-2">
                            <div class="card">
                                <div class="card-body">
                                    <?php $nbSheets = getNbPublishedword() ?>
                                    <h5 class="card-title"><?php echo $nbSheets ?></h5>
                                    <?php if ($nbSheets == 1) : ?>
                                        <p class="card-text">Nombres de mots</p>
                                    <?php else : ?>
                                        <p class="card-text">Nombres de mots</p>
                                    <?php endif ?>
                                </div>
                            </div>
                        </div>
    </main>
  </div>
</div>


    <script src="static/js/bootstrap.bundle.min.js"></script>

      <script src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/feather.min.js" integrity="sha384-uO3SXW5IuS1ZpFPKugNNWqTZRRglnUJK6UAZ/gxOX80nxEkN9NcGZTftn6RzhGWE" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.4/dist/Chart.min.js" integrity="sha384-zNy6FEbO50N+Cg5wap8IKA4M/ZnLJgzc6w2NqACZaK0u0FXfOWRRJOnQtpZun8ha" crossorigin="anonymous"></script><script src="static/js/dashboard.js"></script>
  </body>
</html>
