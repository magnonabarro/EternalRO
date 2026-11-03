-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 30-Jan-2022 às 23:37
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 7.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bleachrpg`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `rmt_logs`
--

CREATE TABLE `rmt_logs` (
  `id` int(11) UNSIGNED NOT NULL,
  `account_id` int(11) UNSIGNED NOT NULL,
  `userid` varchar(23) NOT NULL DEFAULT '',
  `chave_pix` char(100) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `cpf` char(20) NOT NULL,
  `valor` varchar(20) NOT NULL,
  `data_transacao` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `check_transacao` int(11) NOT NULL DEFAULT 1
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `rmt_logs`
--
--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `rmt_logs`
--
ALTER TABLE `rmt_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `name` (`userid`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `rmt_logs`
--
ALTER TABLE `rmt_logs`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
