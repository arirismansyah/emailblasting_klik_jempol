-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 09, 2021 at 08:32 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `klik_jempol`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id_customer` int(11) NOT NULL,
  `nama` varchar(200) NOT NULL,
  `jenis_kelamin` char(1) DEFAULT NULL,
  `tempat_lahir` varchar(200) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `pendidikan` varchar(200) DEFAULT NULL,
  `pekerjaan` varchar(200) DEFAULT NULL,
  `jenis_pakaerjaan` varchar(200) DEFAULT NULL,
  `alamat_domisili` text DEFAULT NULL,
  `prov_domisili` varchar(200) DEFAULT NULL,
  `kab_domisili` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `kabkot`
--

CREATE TABLE `kabkot` (
  `id_kabkot` int(11) NOT NULL,
  `kode_prov` int(11) NOT NULL,
  `nama_kabkot` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kabkot`
--

INSERT INTO `kabkot` (`id_kabkot`, `kode_prov`, `nama_kabkot`) VALUES
(1, 11, ' Kabupaten Aceh Barat'),
(2, 11, ' Kabupaten Aceh Barat Daya'),
(3, 11, ' Kabupaten Aceh Besar'),
(4, 11, ' Kabupaten Aceh Jaya'),
(5, 11, ' Kabupaten Aceh Selatan'),
(6, 11, ' Kabupaten Aceh Singkil'),
(7, 11, ' Kabupaten Aceh Tamiang'),
(8, 11, ' Kabupaten Aceh Tengah'),
(9, 11, ' Kabupaten Aceh Tenggara'),
(10, 11, ' Kabupaten Aceh Timur'),
(11, 11, ' Kabupaten Aceh Utara'),
(12, 11, ' Kabupaten Bener Meriah'),
(13, 11, ' Kabupaten Bireuen'),
(14, 11, ' Kabupaten Gayo Lues'),
(15, 11, ' Kabupaten Nagan Raya'),
(16, 11, ' Kabupaten Pidie'),
(17, 11, ' Kabupaten Pidie Jaya'),
(18, 11, ' Kabupaten Simeulue'),
(19, 11, ' Kota Banda Aceh'),
(20, 11, ' Kota Langsa'),
(21, 11, ' Kota Lhokseumawe'),
(22, 11, ' Kota Sabang'),
(23, 11, ' Kota Subulussalam'),
(24, 12, ' Kabupaten Asahan'),
(25, 12, ' Kabupaten Batubara'),
(26, 12, ' Kabupaten Dairi'),
(27, 12, ' Kabupaten Deli Serdang'),
(28, 12, ' Kabupaten Humbang Hasundutan'),
(29, 12, ' Kabupaten Karo'),
(30, 12, ' Kabupaten Labuhanbatu'),
(31, 12, ' Kabupaten Labuhanbatu Selatan'),
(32, 12, ' Kabupaten Labuhanbatu Utara'),
(33, 12, ' Kabupaten Langkat'),
(34, 12, ' Kabupaten Mandailing Natal'),
(35, 12, ' Kabupaten Nias'),
(36, 12, ' Kabupaten Nias Barat'),
(37, 12, ' Kabupaten Nias Selatan'),
(38, 12, ' Kabupaten Nias Utara'),
(39, 12, ' Kabupaten Padang Lawas'),
(40, 12, ' Kabupaten Padang Lawas Utara'),
(41, 12, ' Kabupaten Pakpak Bharat'),
(42, 12, ' Kabupaten Samosir'),
(43, 12, ' Kabupaten Serdang Bedagai'),
(44, 12, ' Kabupaten Simalungun'),
(45, 12, ' Kabupaten Tapanuli Selatan'),
(46, 12, ' Kabupaten Tapanuli Tengah'),
(47, 12, ' Kabupaten Tapanuli Utara'),
(48, 12, ' Kabupaten Toba Samosir'),
(49, 12, ' Kota Binjai'),
(50, 12, ' Kota Gunungsitoli'),
(51, 12, ' Kota Medan'),
(52, 12, ' Kota Padangsidempuan'),
(53, 12, ' Kota Pematangsiantar'),
(54, 12, ' Kota Sibolga'),
(55, 12, ' Kota Tanjungbalai'),
(56, 12, ' Kota Tebing Tinggi'),
(57, 13, ' Kabupaten Agam'),
(58, 13, ' Kabupaten Dharmasraya'),
(59, 13, ' Kabupaten Kepulauan Mentawai'),
(60, 13, ' Kabupaten Lima Puluh Kota'),
(61, 13, ' Kabupaten Padang Pariaman'),
(62, 13, ' Kabupaten Pasaman'),
(63, 13, ' Kabupaten Pasaman Barat'),
(64, 13, ' Kabupaten Pesisir Selatan'),
(65, 13, ' Kabupaten Sijunjung'),
(66, 13, ' Kabupaten Solok'),
(67, 13, ' Kabupaten Solok Selatan'),
(68, 13, ' Kabupaten Tanah Datar'),
(69, 13, ' Kota Bukittinggi'),
(70, 13, ' Kota Padang'),
(71, 13, ' Kota Padangpanjang'),
(72, 13, ' Kota Pariaman'),
(73, 13, ' Kota Payakumbuh'),
(74, 13, ' Kota Sawahlunto'),
(75, 13, ' Kota Solok'),
(76, 16, ' Kabupaten Banyuasin'),
(77, 16, ' Kabupaten Empat Lawang'),
(78, 16, ' Kabupaten Lahat'),
(79, 16, ' Kabupaten Muara Enim'),
(80, 16, ' Kabupaten Musi Banyuasin'),
(81, 16, ' Kabupaten Musi Rawas'),
(82, 16, ' Kabupaten Musi Rawas Utara'),
(83, 16, ' Kabupaten Ogan Ilir'),
(84, 16, ' Kabupaten Ogan Komering Ilir'),
(85, 16, ' Kabupaten Ogan Komering Ulu'),
(86, 16, ' Kabupaten Ogan Komering Ulu Selatan'),
(87, 16, ' Kabupaten Ogan Komering Ulu Timur'),
(88, 16, ' Kabupaten Penukal Abab Lematang Ilir'),
(89, 16, ' Kota Lubuklinggau'),
(90, 16, ' Kota Pagar Alam'),
(91, 16, ' Kota Palembang'),
(92, 16, ' Kota Prabumulih'),
(93, 14, ' Kabupaten Bengkalis'),
(94, 14, ' Kabupaten Indragiri Hilir'),
(95, 14, ' Kabupaten Indragiri Hulu'),
(96, 14, ' Kabupaten Kampar'),
(97, 14, ' Kabupaten Kepulauan Meranti'),
(98, 14, ' Kabupaten Kuantan Singingi'),
(99, 14, ' Kabupaten Pelalawan'),
(100, 14, ' Kabupaten Rokan Hilir'),
(101, 14, ' Kabupaten Rokan Hulu'),
(102, 14, ' Kabupaten Siak'),
(103, 14, ' Kota Dumai'),
(104, 14, ' Kota Pekanbaru'),
(105, 15, ' Kabupaten Batanghari'),
(106, 15, ' Kabupaten Bungo'),
(107, 15, ' Kabupaten Kerinci'),
(108, 15, ' Kabupaten Merangin'),
(109, 15, ' Kabupaten Muaro Jambi'),
(110, 15, ' Kabupaten Sarolangun'),
(111, 15, ' Kabupaten Tanjung Jabung Barat'),
(112, 15, ' Kabupaten Tanjung Jabung Timur'),
(113, 15, ' Kabupaten Tebo'),
(114, 15, ' Kota Jambi'),
(115, 15, ' Kota Sungai Penuh'),
(116, 17, ' Kabupaten Bengkulu Selatan'),
(117, 17, ' Kabupaten Bengkulu Tengah'),
(118, 17, ' Kabupaten Bengkulu Utara'),
(119, 17, ' Kabupaten Kaur'),
(120, 17, ' Kabupaten Kepahiang'),
(121, 17, ' Kabupaten Lebong'),
(122, 17, ' Kabupaten Mukomuko'),
(123, 17, ' Kabupaten Rejang Lebong'),
(124, 17, ' Kabupaten Seluma'),
(125, 17, ' Kota Bengkulu'),
(126, 18, ' Kabupaten Lampung Tengah'),
(127, 18, ' Kabupaten Lampung Utara'),
(128, 18, ' Kabupaten Lampung Selatan'),
(129, 18, ' Kabupaten Lampung Barat'),
(130, 18, ' Kabupaten Lampung Timur'),
(131, 18, ' Kabupaten Mesuji'),
(132, 18, ' Kabupaten Pesawaran'),
(133, 18, ' Kabupaten Pesisir Barat'),
(134, 18, ' Kabupaten Pringsewu'),
(135, 18, ' Kabupaten Tulang Bawang'),
(136, 18, ' Kabupaten Tulang Bawang Barat'),
(137, 18, ' Kabupaten Tanggamus'),
(138, 18, ' Kabupaten Way Kanan'),
(139, 18, ' Kota Bandar Lampung'),
(140, 18, ' Kota Metro'),
(141, 19, ' Kabupaten Bangka'),
(142, 19, ' Kabupaten Bangka Barat'),
(143, 19, ' Kabupaten Bangka Selatan'),
(144, 19, ' Kabupaten Bangka Tengah'),
(145, 19, ' Kabupaten Belitung'),
(146, 19, ' Kabupaten Belitung Timur'),
(147, 19, ' Kota Pangkal Pinang'),
(148, 21, ' Kabupaten Bintan'),
(149, 21, ' Kabupaten Karimun'),
(150, 21, ' Kabupaten Kepulauan Anambas'),
(151, 21, ' Kabupaten Lingga'),
(152, 21, ' Kabupaten Natuna'),
(153, 21, ' Kota Batam'),
(154, 21, ' Kota Tanjung Pinang'),
(155, 31, ' Kota Administrasi Jakarta Barat'),
(156, 31, ' Kota Administrasi Jakarta Pusat'),
(157, 31, ' Kota Administrasi Jakarta Selatan'),
(158, 31, ' Kota Administrasi Jakarta Timur'),
(159, 31, ' Kota Administrasi Jakarta Utara'),
(160, 31, ' Kabupaten Administrasi Kepulauan Seribu'),
(161, 32, ' Kabupaten Bandung'),
(162, 32, ' Kabupaten Bandung Barat'),
(163, 32, ' Kabupaten Bekasi'),
(164, 32, ' Kabupaten Bogor'),
(165, 32, ' Kabupaten Ciamis'),
(166, 32, ' Kabupaten Cianjur'),
(167, 32, ' Kabupaten Cirebon'),
(168, 32, ' Kabupaten Garut'),
(169, 32, ' Kabupaten Indramayu'),
(170, 32, ' Kabupaten Karawang'),
(171, 32, ' Kabupaten Kuningan'),
(172, 32, ' Kabupaten Majalengka'),
(173, 32, ' Kabupaten Pangandaran'),
(174, 32, ' Kabupaten Purwakarta'),
(175, 32, ' Kabupaten Subang'),
(176, 32, ' Kabupaten Sukabumi'),
(177, 32, ' Kabupaten Sumedang'),
(178, 32, ' Kabupaten Tasikmalaya'),
(179, 32, ' Kota Bandung'),
(180, 32, ' Kota Banjar'),
(181, 32, ' Kota Bekasi'),
(182, 32, ' Kota Bogor'),
(183, 32, ' Kota Cimahi'),
(184, 32, ' Kota Cirebon'),
(185, 32, ' Kota Depok'),
(186, 32, ' Kota Sukabumi'),
(187, 32, ' Kota Tasikmalaya'),
(188, 33, ' Kabupaten Banjarnegara'),
(189, 33, ' Kabupaten Banyumas'),
(190, 33, ' Kabupaten Batang'),
(191, 33, ' Kabupaten Blora'),
(192, 33, ' Kabupaten Boyolali'),
(193, 33, ' Kabupaten Brebes'),
(194, 33, ' Kabupaten Cilacap'),
(195, 33, ' Kabupaten Demak'),
(196, 33, ' Kabupaten Grobogan'),
(197, 33, ' Kabupaten Jepara'),
(198, 33, ' Kabupaten Karanganyar'),
(199, 33, ' Kabupaten Kebumen'),
(200, 33, ' Kabupaten Kendal'),
(201, 33, ' Kabupaten Klaten'),
(202, 33, ' Kabupaten Kudus'),
(203, 33, ' Kabupaten Magelang'),
(204, 33, ' Kabupaten Pati'),
(205, 33, ' Kabupaten Pekalongan'),
(206, 33, ' Kabupaten Pemalang'),
(207, 33, ' Kabupaten Purbalingga'),
(208, 33, ' Kabupaten Purworejo'),
(209, 33, ' Kabupaten Rembang'),
(210, 33, ' Kabupaten Semarang'),
(211, 33, ' Kabupaten Sragen'),
(212, 33, ' Kabupaten Sukoharjo'),
(213, 33, ' Kabupaten Tegal'),
(214, 33, ' Kabupaten Temanggung'),
(215, 33, ' Kabupaten Wonogiri'),
(216, 33, ' Kabupaten Wonosobo'),
(217, 33, ' Kota Magelang'),
(218, 33, ' Kota Pekalongan'),
(219, 33, ' Kota Salatiga'),
(220, 33, ' Kota Semarang'),
(221, 33, ' Kota Surakarta'),
(222, 33, ' Kota Tegal'),
(223, 34, ' Kabupaten Bantul'),
(224, 34, ' Kabupaten Gunungkidul'),
(225, 34, ' Kabupaten Kulon Progo'),
(226, 34, ' Kabupaten Sleman'),
(227, 34, ' Kota Yogyakarta'),
(228, 35, ' Kabupaten Bangkalan'),
(229, 35, ' Kabupaten Banyuwangi'),
(230, 35, ' Kabupaten Blitar'),
(231, 35, ' Kabupaten Bojonegoro'),
(232, 35, ' Kabupaten Bondowoso'),
(233, 35, ' Kabupaten Gresik'),
(234, 35, ' Kabupaten Jember'),
(235, 35, ' Kabupaten Jombang'),
(236, 35, ' Kabupaten Kediri'),
(237, 35, ' Kabupaten Lamongan'),
(238, 35, ' Kabupaten Lumajang'),
(239, 35, ' Kabupaten Madiun'),
(240, 35, ' Kabupaten Magetan'),
(241, 35, ' Kabupaten Malang'),
(242, 35, ' Kabupaten Mojokerto'),
(243, 35, ' Kabupaten Nganjuk'),
(244, 35, ' Kabupaten Ngawi'),
(245, 35, ' Kabupaten Pacitan'),
(246, 35, ' Kabupaten Pamekasan'),
(247, 35, ' Kabupaten Pasuruan'),
(248, 35, ' Kabupaten Ponorogo'),
(249, 35, ' Kabupaten Probolinggo'),
(250, 35, ' Kabupaten Sampang'),
(251, 35, ' Kabupaten Sidoarjo'),
(252, 35, ' Kabupaten Situbondo'),
(253, 35, ' Kabupaten Sumenep'),
(254, 35, ' Kabupaten Trenggalek'),
(255, 35, ' Kabupaten Tuban'),
(256, 35, ' Kabupaten Tulungagung'),
(257, 35, ' Kota Batu'),
(258, 35, ' Kota Blitar'),
(259, 35, ' Kota Kediri'),
(260, 35, ' Kota Madiun'),
(261, 35, ' Kota Malang'),
(262, 35, ' Kota Mojokerto'),
(263, 35, ' Kota Pasuruan'),
(264, 35, ' Kota Probolinggo'),
(265, 35, ' Kota Surabaya'),
(266, 36, ' Kabupaten Lebak'),
(267, 36, ' Kabupaten Pandeglang'),
(268, 36, ' Kabupaten Serang'),
(269, 36, ' Kabupaten Tangerang'),
(270, 36, ' Kota Cilegon'),
(271, 36, ' Kota Serang'),
(272, 36, ' Kota Tangerang'),
(273, 36, ' Kota Tangerang Selatan'),
(274, 51, ' Kabupaten Badung'),
(275, 51, ' Kabupaten Bangli'),
(276, 51, ' Kabupaten Buleleng'),
(277, 51, ' Kabupaten Gianyar'),
(278, 51, ' Kabupaten Jembrana'),
(279, 51, ' Kabupaten Karangasem'),
(280, 51, ' Kabupaten Klungkung'),
(281, 51, ' Kabupaten Tabanan'),
(282, 51, ' Kota Denpasar'),
(283, 52, ' Kabupaten Bima'),
(284, 52, ' Kabupaten Dompu'),
(285, 52, ' Kabupaten Lombok Barat'),
(286, 52, ' Kabupaten Lombok Tengah'),
(287, 52, ' Kabupaten Lombok Timur'),
(288, 52, ' Kabupaten Lombok Utara'),
(289, 52, ' Kabupaten Sumbawa'),
(290, 52, ' Kabupaten Sumbawa Barat'),
(291, 52, ' Kota Bima'),
(292, 52, ' Kota Mataram'),
(293, 53, ' Kabupaten Alor'),
(294, 53, ' Kabupaten Belu'),
(295, 53, ' Kabupaten Ende'),
(296, 53, ' Kabupaten Flores Timur'),
(297, 53, ' Kabupaten Kupang'),
(298, 53, ' Kabupaten Lembata'),
(299, 53, ' Kabupaten Malaka'),
(300, 53, ' Kabupaten Manggarai'),
(301, 53, ' Kabupaten Manggarai Barat'),
(302, 53, ' Kabupaten Manggarai Timur'),
(303, 53, ' Kabupaten Ngada'),
(304, 53, ' Kabupaten Nagekeo'),
(305, 53, ' Kabupaten Rote Ndao'),
(306, 53, ' Kabupaten Sabu Raijua'),
(307, 53, ' Kabupaten Sikka'),
(308, 53, ' Kabupaten Sumba Barat'),
(309, 53, ' Kabupaten Sumba Barat Daya'),
(310, 53, ' Kabupaten Sumba Tengah'),
(311, 53, ' Kabupaten Sumba Timur'),
(312, 53, ' Kabupaten Timor Tengah Selatan'),
(313, 53, ' Kabupaten Timor Tengah Utara'),
(314, 53, ' Kota Kupang'),
(315, 61, ' Kabupaten Bengkayang'),
(316, 61, ' Kabupaten Kapuas Hulu'),
(317, 61, ' Kabupaten Kayong Utara'),
(318, 61, ' Kabupaten Ketapang'),
(319, 61, ' Kabupaten Kubu Raya'),
(320, 61, ' Kabupaten Landak'),
(321, 61, ' Kabupaten Melawi'),
(322, 61, ' Kabupaten Mempawah'),
(323, 61, ' Kabupaten Sambas'),
(324, 61, ' Kabupaten Sanggau'),
(325, 61, ' Kabupaten Sekadau'),
(326, 61, ' Kabupaten Sintang'),
(327, 61, ' Kota Pontianak'),
(328, 61, ' Kota Singkawang'),
(329, 62, ' Kabupaten Barito Selatan'),
(330, 62, ' Kabupaten Barito Timur'),
(331, 62, ' Kabupaten Barito Utara'),
(332, 62, ' Kabupaten Gunung Mas'),
(333, 62, ' Kabupaten Kapuas'),
(334, 62, ' Kabupaten Katingan'),
(335, 62, ' Kabupaten Kotawaringin Barat'),
(336, 62, ' Kabupaten Kotawaringin Timur'),
(337, 62, ' Kabupaten Lamandau'),
(338, 62, ' Kabupaten Murung Raya'),
(339, 62, ' Kabupaten Pulang Pisau'),
(340, 62, ' Kabupaten Sukamara'),
(341, 62, ' Kabupaten Seruyan'),
(342, 62, ' Kota Palangka Raya'),
(343, 63, ' Kabupaten Balangan'),
(344, 63, ' Kabupaten Banjar'),
(345, 63, ' Kabupaten Barito Kuala'),
(346, 63, ' Kabupaten Hulu Sungai Selatan'),
(347, 63, ' Kabupaten Hulu Sungai Tengah'),
(348, 63, ' Kabupaten Hulu Sungai Utara'),
(349, 63, ' Kabupaten Kotabaru'),
(350, 63, ' Kabupaten Tabalong'),
(351, 63, ' Kabupaten Tanah Bumbu'),
(352, 63, ' Kabupaten Tanah Laut'),
(353, 63, ' Kabupaten Tapin'),
(354, 63, ' Kota Banjarbaru'),
(355, 63, ' Kota Banjarmasin'),
(356, 64, ' Kabupaten Berau'),
(357, 64, ' Kabupaten Kutai Barat'),
(358, 64, ' Kabupaten Kutai Kartanegara'),
(359, 64, ' Kabupaten Kutai Timur'),
(360, 64, ' Kabupaten Mahakam Ulu'),
(361, 64, ' Kabupaten Paser'),
(362, 64, ' Kabupaten Penajam Paser Utara'),
(363, 64, ' Kota Balikpapan'),
(364, 64, ' Kota Bontang'),
(365, 64, ' Kota Samarinda'),
(366, 65, ' Kabupaten Bulungan'),
(367, 65, ' Kabupaten Malinau'),
(368, 65, ' Kabupaten Nunukan'),
(369, 65, ' Kabupaten Tana Tidung'),
(370, 65, ' Kota Tarakan'),
(371, 71, ' Kabupaten Bombana'),
(372, 71, ' Kabupaten Buton'),
(373, 71, ' Kabupaten Buton Selatan'),
(374, 71, ' Kabupaten Buton Tengah'),
(375, 71, ' Kabupaten Buton Utara'),
(376, 71, ' Kabupaten Kolaka'),
(377, 71, ' Kabupaten Kolaka Timur'),
(378, 71, ' Kabupaten Kolaka Utara'),
(379, 71, ' Kabupaten Konawe'),
(380, 71, ' Kabupaten Konawe Kepulauan'),
(381, 71, ' Kabupaten Konawe Selatan'),
(382, 71, ' Kabupaten Konawe Utara'),
(383, 71, ' Kabupaten Muna'),
(384, 71, ' Kabupaten Muna Barat'),
(385, 71, ' Kabupaten Wakatobi'),
(386, 71, ' Kota Bau-Bau'),
(387, 71, ' Kota Kendari'),
(388, 72, ' Kabupaten Banggai'),
(389, 72, ' Kabupaten Banggai Kepulauan'),
(390, 72, ' Kabupaten Banggai Laut'),
(391, 72, ' Kabupaten Buol'),
(392, 72, ' Kabupaten Donggala'),
(393, 72, ' Kabupaten Morowali'),
(394, 72, ' Kabupaten Morowali Utara'),
(395, 72, ' Kabupaten Parigi Moutong'),
(396, 72, ' Kabupaten Poso'),
(397, 72, ' Kabupaten Sigi'),
(398, 72, ' Kabupaten Tojo Una-Una'),
(399, 72, ' Kabupaten Toli-Toli'),
(400, 72, ' Kota Palu'),
(401, 73, ' Kabupaten Bantaeng'),
(402, 73, ' Kabupaten Barru'),
(403, 73, ' Kabupaten Bone'),
(404, 73, ' Kabupaten Bulukumba'),
(405, 73, ' Kabupaten Enrekang'),
(406, 73, ' Kabupaten Gowa'),
(407, 73, ' Kabupaten Jeneponto'),
(408, 73, ' Kabupaten Kepulauan Selayar'),
(409, 73, ' Kabupaten Luwu'),
(410, 73, ' Kabupaten Luwu Timur'),
(411, 73, ' Kabupaten Luwu Utara'),
(412, 73, ' Kabupaten Maros'),
(413, 73, ' Kabupaten Pangkajene dan Kepulauan'),
(414, 73, ' Kabupaten Pinrang'),
(415, 73, ' Kabupaten Sidenreng Rappang'),
(416, 73, ' Kabupaten Sinjai'),
(417, 73, ' Kabupaten Soppeng'),
(418, 73, ' Kabupaten Takalar'),
(419, 73, ' Kabupaten Tana Toraja'),
(420, 73, ' Kabupaten Toraja Utara'),
(421, 73, ' Kabupaten Wajo'),
(422, 73, ' Kota Makassar'),
(423, 73, ' Kota Palopo'),
(424, 73, ' Kota Parepare'),
(425, 74, ' Kabupaten Bombana'),
(426, 74, ' Kabupaten Buton'),
(427, 74, ' Kabupaten Buton Selatan'),
(428, 74, ' Kabupaten Buton Tengah'),
(429, 74, ' Kabupaten Buton Utara'),
(430, 74, ' Kabupaten Kolaka'),
(431, 74, ' Kabupaten Kolaka Timur'),
(432, 74, ' Kabupaten Kolaka Utara'),
(433, 74, ' Kabupaten Konawe'),
(434, 74, ' Kabupaten Konawe Kepulauan'),
(435, 74, ' Kabupaten Konawe Selatan'),
(436, 74, ' Kabupaten Konawe Utara'),
(437, 74, ' Kabupaten Muna'),
(438, 74, ' Kabupaten Muna Barat'),
(439, 74, ' Kabupaten Wakatobi'),
(440, 74, ' Kota Bau-Bau'),
(441, 74, ' Kota Kendari'),
(442, 75, ' Kabupaten Boalemo'),
(443, 75, ' Kabupaten Bone Bolango'),
(444, 75, ' Kabupaten Gorontalo'),
(445, 75, ' Kabupaten Gorontalo Utara'),
(446, 75, ' Kabupaten Pohuwato'),
(447, 75, ' Kota Gorontalo'),
(448, 76, ' Kabupaten Majene'),
(449, 76, ' Kabupaten Mamasa'),
(450, 76, ' Kabupaten Mamuju'),
(451, 76, ' Kabupaten Mamuju Tengah'),
(452, 76, ' Kabupaten Mamuju Utara'),
(453, 76, ' Kabupaten Polewali Mandar'),
(454, 76, ' Kota Mamuju'),
(455, 81, ' Kabupaten Buru'),
(456, 81, ' Kabupaten Buru Selatan'),
(457, 81, ' Kabupaten Kepulauan Aru'),
(458, 81, ' Kabupaten Maluku Barat Daya'),
(459, 81, ' Kabupaten Maluku Tengah'),
(460, 81, ' Kabupaten Maluku Tenggara'),
(461, 81, ' Kabupaten Maluku Tenggara Barat'),
(462, 81, ' Kabupaten Seram Bagian Barat'),
(463, 81, ' Kabupaten Seram Bagian Timur'),
(464, 81, ' Kota Ambon'),
(465, 81, ' Kota Tual'),
(466, 82, ' Kabupaten Halmahera Barat'),
(467, 82, ' Kabupaten Halmahera Tengah'),
(468, 82, ' Kabupaten Halmahera Utara'),
(469, 82, ' Kabupaten Halmahera Selatan'),
(470, 82, ' Kabupaten Kepulauan Sula'),
(471, 82, ' Kabupaten Halmahera Timur'),
(472, 82, ' Kabupaten Pulau Morotai'),
(473, 82, ' Kabupaten Pulau Taliabu'),
(474, 82, ' Kota Ternate'),
(475, 82, ' Kota Tidore Kepulauan'),
(476, 91, ' Kabupaten Fakfak'),
(477, 91, ' Kabupaten Kaimana'),
(478, 91, ' Kabupaten Manokwari'),
(479, 91, ' Kabupaten Manokwari Selatan'),
(480, 91, ' Kabupaten Maybrat'),
(481, 91, ' Kabupaten Pegunungan Arfak'),
(482, 91, ' Kabupaten Raja Ampat'),
(483, 91, ' Kabupaten Sorong'),
(484, 91, ' Kabupaten Sorong Selatan'),
(485, 91, ' Kabupaten Tambrauw'),
(486, 91, ' Kabupaten Teluk Bintuni'),
(487, 91, ' Kabupaten Teluk Wondama'),
(488, 94, ' Kabupaten Asmat'),
(489, 94, ' Kabupaten Biak Numfor'),
(490, 94, ' Kabupaten Boven Digoel'),
(491, 94, ' Kabupaten Deiyai'),
(492, 94, ' Kabupaten Dogiyai'),
(493, 94, ' Kabupaten Intan Jaya'),
(494, 94, ' Kabupaten Jayapura'),
(495, 94, ' Kabupaten Jayawijaya'),
(496, 94, ' Kabupaten Keerom'),
(497, 94, ' Kabupaten Kepulauan Yapen'),
(498, 94, ' Kabupaten Lanny Jaya'),
(499, 94, ' Kabupaten Mamberamo Raya'),
(500, 94, ' Kabupaten Mamberamo Tengah'),
(501, 94, ' Kabupaten Mappi'),
(502, 94, ' Kabupaten Merauke'),
(503, 94, ' Kabupaten Mimika'),
(504, 94, ' Kabupaten Nabire'),
(505, 94, ' Kabupaten Nduga'),
(506, 94, ' Kabupaten Paniai'),
(507, 94, ' Kabupaten Pegunungan Bintang'),
(508, 94, ' Kabupaten Puncak'),
(509, 94, ' Kabupaten Puncak Jaya'),
(510, 94, ' Kabupaten Sarmi'),
(511, 94, ' Kabupaten Supiori'),
(512, 94, ' Kabupaten Tolikara'),
(513, 94, ' Kabupaten Waropen'),
(514, 94, ' Kabupaten Yahukimo'),
(515, 94, ' Kabupaten Yalimo'),
(516, 94, ' Kota Jayapura');

-- --------------------------------------------------------

--
-- Table structure for table `log_email`
--

CREATE TABLE `log_email` (
  `id_log` int(11) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `id_customer` int(11) NOT NULL,
  `nama_receiver` varchar(200) NOT NULL,
  `email_receiver` varchar(200) NOT NULL,
  `sent_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` varchar(50) NOT NULL,
  `keterangan` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `prov`
--

CREATE TABLE `prov` (
  `kode_prov` int(11) NOT NULL,
  `nama_prov` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prov`
--

INSERT INTO `prov` (`kode_prov`, `nama_prov`) VALUES
(11, 'Aceh'),
(12, 'Sumatera Utara'),
(13, 'Sumatera Barat'),
(14, 'Riau'),
(15, 'Jambi'),
(16, 'Sumatera Selatan'),
(17, 'Bengkulu'),
(18, 'Lampung'),
(19, 'Kep. Bangka Belitung'),
(21, 'Kep. Riau'),
(31, 'DKI Jakarta'),
(32, 'Jawa Barat'),
(33, 'Jawa Tengah'),
(34, 'DI Yogyakarta'),
(35, 'Jawa Timur'),
(36, 'Banten'),
(51, 'Bali'),
(52, 'Nusa Tenggara Barat'),
(53, 'Nusa Tenggara Timur'),
(61, 'Kalimantan Barat'),
(62, 'Kalimantan Tengah'),
(63, 'Kalimantan Selatan'),
(64, 'Kalimantan Timur'),
(65, 'Kalimantan Utara'),
(71, 'Sulawesi Utara'),
(72, 'Sulawesi Tengah'),
(73, 'Sulawesi Selatan'),
(74, 'Sulawesi Tenggara'),
(75, 'Gorontalo'),
(76, 'Sulawesi Barat'),
(81, 'Maluku'),
(82, 'Maluku Utara'),
(91, 'Papua Barat'),
(94, 'Papua');

-- --------------------------------------------------------

--
-- Table structure for table `template_email`
--

CREATE TABLE `template_email` (
  `id_template` int(11) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `body` text NOT NULL,
  `nama_produk` varchar(200) NOT NULL,
  `lampiran` varchar(200) NOT NULL,
  `status` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id_customer`);

--
-- Indexes for table `kabkot`
--
ALTER TABLE `kabkot`
  ADD PRIMARY KEY (`id_kabkot`);

--
-- Indexes for table `log_email`
--
ALTER TABLE `log_email`
  ADD PRIMARY KEY (`id_log`);

--
-- Indexes for table `prov`
--
ALTER TABLE `prov`
  ADD PRIMARY KEY (`kode_prov`);

--
-- Indexes for table `template_email`
--
ALTER TABLE `template_email`
  ADD PRIMARY KEY (`id_template`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id_customer` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `kabkot`
--
ALTER TABLE `kabkot`
  MODIFY `id_kabkot` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=517;

--
-- AUTO_INCREMENT for table `log_email`
--
ALTER TABLE `log_email`
  MODIFY `id_log` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `template_email`
--
ALTER TABLE `template_email`
  MODIFY `id_template` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
