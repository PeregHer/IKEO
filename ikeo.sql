-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Nov 22, 2020 at 12:11 AM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ikeo`
--
CREATE DATABASE IF NOT EXISTS `ikeo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ikeo`;

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `clients` (
  `id_client` int(11) NOT NULL,
  `type_client` int(11) NOT NULL,
  `nom_client` varchar(50) NOT NULL,
  `adresse_client` varchar(50) NOT NULL,
  `ville_client` varchar(50) NOT NULL,
  `pays_client` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `clients`
--

INSERT INTO `clients` (`id_client`, `type_client`, `nom_client`, `adresse_client`, `ville_client`, `pays_client`) VALUES
(1, 1, 'Bo Meuble', 'Place Vendôme', 'Paris', 1),
(2, 1, 'Mobel', 'Porte de Brandebourg ', 'Berlin', 2),
(3, 1, 'Bo Meuble', 'Rue Jean Jaurès', 'Brest', 1),
(4, 1, 'Tout A La Maison', 'Rue de la Bastille', 'Paris', 1),
(5, 1, 'Bo Meuble', 'Avenue des Trois Dragons', 'Barcelone', 3),
(6, 2, 'The World Compagny', 'Oxford street', 'Londres', 4),
(7, 1, 'The Best Greatest Beautifulest Furniture', 'Coven Garden ', 'Londres', 4),
(8, 1, 'Ikeo', 'Yolo', 'Brest', 1);

-- --------------------------------------------------------

--
-- Table structure for table `factures`
--

CREATE TABLE `factures` (
  `id_facture` varchar(8) NOT NULL,
  `date_facture` date NOT NULL,
  `id_client` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `factures`
--

INSERT INTO `factures` (`id_facture`, `date_facture`, `id_client`) VALUES
('MSQ291', '2018-06-15', 1),
('MSQ292', '2018-06-23', 5),
('MSQ293', '2018-06-23', 6),
('MSQ294', '2018-06-28', 1),
('MSQ295', '2018-07-01', 4),
('MSQ296', '2018-07-04', 7),
('MSQ297', '2018-07-12', 2);

-- --------------------------------------------------------

--
-- Table structure for table `facture_produit`
--

CREATE TABLE `facture_produit` (
  `id_facture` varchar(11) NOT NULL,
  `id_produit` varchar(11) NOT NULL,
  `quantite_produit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `facture_produit`
--

INSERT INTO `facture_produit` (`id_facture`, `id_produit`, `quantite_produit`) VALUES
('MSQ291', 'OANT72', 20),
('MSQ291', 'LXAL34', 30),
('MSQ291', 'OANT67', 10),
('MSQ292', 'OANT90', 25),
('MSQ292', 'LXAL34', 32),
('MSQ293', 'OANT67', 80),
('MSQ293', 'LXAL56', 70),
('MSQ293', 'LXAL78', 60),
('MSQ293', 'LXAL34', 120),
('MSQ293', 'LXAL12', 90),
('MSQ294', 'OANT72', 10),
('MSQ294', 'OANT34', 10),
('MSQ294', 'LXAL78', 30),
('MSQ295', 'OANT72', 25),
('MSQ295', 'LXAL12', 34),
('MSQ296', 'OANT34', 40),
('MSQ296', 'LXAL56', 38),
('MSQ296', 'LXAL78', 54),
('MSQ297', 'LXAL34', 20),
('MSQ297', 'LXAL56', 34),
('MSQ297', 'LXAL78', 45);

-- --------------------------------------------------------

--
-- Table structure for table `pays`
--

CREATE TABLE `pays` (
  `id_pays` int(11) NOT NULL,
  `nom_pays` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pays`
--

INSERT INTO `pays` (`id_pays`, `nom_pays`) VALUES
(1, 'France'),
(2, 'Allemagne'),
(3, 'Espagne'),
(4, 'Angleterre');

-- --------------------------------------------------------

--
-- Table structure for table `produits`
--

CREATE TABLE `produits` (
  `id_produit` varchar(8) NOT NULL,
  `nom_produit` varchar(50) NOT NULL,
  `desc_produit` text NOT NULL,
  `statut_produit` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `produits`
--

INSERT INTO `produits` (`id_produit`, `nom_produit`, `desc_produit`, `statut_produit`) VALUES
('LXAL12', 'Dahl', 'Tiroir à rond de serviette', 0),
('LXAL34', 'Gulbrandsen', 'Lit nuage en lévitation ', 1),
('LXAL56', 'Naess', 'Table 128 convives ', 1),
('LXAL78', 'Lund', 'Bureau-cafetière électrique', 1),
('OANT12', 'Apfelgluk', 'Panier à chien (ou à chat) ', 1),
('OANT34', 'Moen', 'Chaise haute de bar', 0),
('OANT67', 'Eide', 'Porte-serviettes pour 100 serviettes', 1),
('OANT72', 'Knutsen', 'Table basse pour poser les bières', 1),
('OANT90', 'Ruud', 'Bureau-lit conbiné', 1);

-- --------------------------------------------------------

--
-- Table structure for table `produit_site`
--

CREATE TABLE `produit_site` (
  `id_produit` varchar(8) NOT NULL,
  `id_site` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `produit_site`
--

INSERT INTO `produit_site` (`id_produit`, `id_site`) VALUES
('OANT72', 1),
('OANT72', 2),
('OANT34', 1),
('OANT34', 2),
('OANT67', 1),
('OANT67', 3),
('LXAL34', 3),
('LXAL56', 1),
('LXAL56', 2),
('LXAL56', 3),
('OANT90', 3),
('OANT12', 3);

-- --------------------------------------------------------

--
-- Table structure for table `sites`
--

CREATE TABLE `sites` (
  `id_site` int(11) NOT NULL,
  `nom_site` varchar(50) NOT NULL,
  `adresse_site` varchar(50) NOT NULL,
  `ville_site` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sites`
--

INSERT INTO `sites` (`id_site`, `nom_site`, `adresse_site`, `ville_site`) VALUES
(1, 'Harald', 'Quai Pipervika', 'Oslo'),
(2, 'Sverre', 'Rue Strangehagen', 'Bergen'),
(3, 'Olaf', 'Place Nidaros', 'Trondheim');

-- --------------------------------------------------------

--
-- Table structure for table `type_client`
--

CREATE TABLE `type_client` (
  `id_type` int(11) NOT NULL,
  `nom_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `type_client`
--

INSERT INTO `type_client` (`id_type`, `nom_type`) VALUES
(1, 'Magasin'),
(2, 'Central d\'achat');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id_client`),
  ADD KEY `pays_client` (`pays_client`),
  ADD KEY `type_client` (`type_client`);

--
-- Indexes for table `factures`
--
ALTER TABLE `factures`
  ADD PRIMARY KEY (`id_facture`),
  ADD KEY `id_client` (`id_client`);

--
-- Indexes for table `facture_produit`
--
ALTER TABLE `facture_produit`
  ADD KEY `id_facture` (`id_facture`),
  ADD KEY `id_produit` (`id_produit`);

--
-- Indexes for table `pays`
--
ALTER TABLE `pays`
  ADD PRIMARY KEY (`id_pays`);

--
-- Indexes for table `produits`
--
ALTER TABLE `produits`
  ADD PRIMARY KEY (`id_produit`);

--
-- Indexes for table `produit_site`
--
ALTER TABLE `produit_site`
  ADD KEY `id_site` (`id_site`),
  ADD KEY `id_produit` (`id_produit`);

--
-- Indexes for table `sites`
--
ALTER TABLE `sites`
  ADD PRIMARY KEY (`id_site`);

--
-- Indexes for table `type_client`
--
ALTER TABLE `type_client`
  ADD PRIMARY KEY (`id_type`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clients`
--
ALTER TABLE `clients`
  MODIFY `id_client` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `pays`
--
ALTER TABLE `pays`
  MODIFY `id_pays` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `sites`
--
ALTER TABLE `sites`
  MODIFY `id_site` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `type_client`
--
ALTER TABLE `type_client`
  MODIFY `id_type` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `clients`
--
ALTER TABLE `clients`
  ADD CONSTRAINT `clients_ibfk_1` FOREIGN KEY (`pays_client`) REFERENCES `pays` (`id_pays`),
  ADD CONSTRAINT `clients_ibfk_2` FOREIGN KEY (`type_client`) REFERENCES `type_client` (`id_type`);

--
-- Constraints for table `factures`
--
ALTER TABLE `factures`
  ADD CONSTRAINT `factures_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `clients` (`id_client`);

--
-- Constraints for table `facture_produit`
--
ALTER TABLE `facture_produit`
  ADD CONSTRAINT `facture_produit_ibfk_1` FOREIGN KEY (`id_facture`) REFERENCES `factures` (`id_facture`),
  ADD CONSTRAINT `facture_produit_ibfk_2` FOREIGN KEY (`id_produit`) REFERENCES `produits` (`id_produit`);

--
-- Constraints for table `produit_site`
--
ALTER TABLE `produit_site`
  ADD CONSTRAINT `produit_site_ibfk_1` FOREIGN KEY (`id_site`) REFERENCES `sites` (`id_site`),
  ADD CONSTRAINT `produit_site_ibfk_2` FOREIGN KEY (`id_produit`) REFERENCES `produits` (`id_produit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
