-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: abarrotes_db
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `almacen`
--

DROP TABLE IF EXISTS `almacen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `almacen` (
  `id_almacen` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_almacen`),
  UNIQUE KEY `id_almacen_UNIQUE` (`id_almacen`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `almacen`
--

LOCK TABLES `almacen` WRITE;
/*!40000 ALTER TABLE `almacen` DISABLE KEYS */;
INSERT INTO `almacen` VALUES (1,'Almacen Principal','dev','2022-02-20 08:09:22',1),(2,'Almacen Secundario_upd','dev','2022-02-20 08:09:31',0);
/*!40000 ALTER TABLE `almacen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_tokens`
--

DROP TABLE IF EXISTS `api_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_tokens` (
  `id_api_tokens` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `jti` varchar(1023) COLLATE utf8_spanish_ci NOT NULL,
  `tipo_token` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_expiracion` datetime NOT NULL,
  `activo` tinyint NOT NULL,
  PRIMARY KEY (`id_api_tokens`),
  UNIQUE KEY `id_api_tokens_UNIQUE` (`id_api_tokens`),
  KEY `id_usuario_ibfk_n_idx` (`id_usuario`),
  CONSTRAINT `id_usuario_ibfk_n` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_entidad`)
) ENGINE=InnoDB AUTO_INCREMENT=267 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_tokens`
--

LOCK TABLES `api_tokens` WRITE;
/*!40000 ALTER TABLE `api_tokens` DISABLE KEYS */;
INSERT INTO `api_tokens` VALUES (1,1,'5dce2374-61a7-4470-8390-50982847ec8d','access','2022-02-10 17:10:06',1),(2,1,'b1083983-6693-4d77-bbb0-5b63610d9796','refresh','2022-03-12 16:55:06',1),(3,1,'7eecf5fb-3efa-4fa0-9a8b-cda85e4e22dc','access','2022-02-10 22:38:42',1),(4,1,'f494c17b-c551-4d06-bb34-4e9c06b51ce4','refresh','2022-03-12 22:23:42',1),(5,1,'46deda43-bb03-4a58-b85f-e32102c656da','access','2022-02-10 23:02:40',0),(6,1,'fc99270f-2ba0-40b7-8b59-ce0baf5edd4b','refresh','2022-03-12 22:47:40',0),(7,1,'c7794fa5-47a7-47d1-9dde-5c1904f56afe','access','2022-02-10 23:19:04',0),(8,1,'d0a38a7b-794a-4c24-83f8-b68e5ca2b262','refresh','2022-03-12 23:04:04',0),(9,1,'96bbafbd-8477-448a-9533-3372cc9aa933','access','2022-02-10 23:39:15',0),(10,1,'848994a4-7d70-4e83-80ee-eb80951c1f8b','refresh','2022-03-12 23:24:15',0),(11,1,'824c4c1f-44eb-4c87-b9ed-d669fd225e64','access','2022-02-11 00:18:35',0),(12,1,'a81ca2bc-9b5c-4fe1-8bce-efb131b35296','refresh','2022-03-13 00:03:35',0),(13,1,'c44590f4-f139-4f4f-b6c9-4761a218136d','access','2022-02-11 00:31:14',0),(14,1,'62a015ff-f2e4-4d1f-8a72-b1827067780d','refresh','2022-03-13 00:16:14',0),(15,1,'b1e0007c-1d9b-4bd9-856c-a9b8c9a7b202','access','2022-02-14 00:36:16',0),(16,1,'4c26d817-60d7-4953-8a78-bb279dd13f53','refresh','2022-03-16 00:21:16',0),(17,1,'7a0b2f38-4dd1-44f2-ae2c-3cba30d46781','access','2022-02-14 01:03:57',0),(18,1,'f0b11f6f-a271-4de2-80b0-9b9b6a4825d7','refresh','2022-03-16 00:48:57',0),(19,1,'f0e1213f-5176-464e-8e31-5817a1e565b9','access','2022-02-14 01:10:22',0),(20,1,'2b2bacb7-37ab-4d33-b34f-62f72fa16287','refresh','2022-03-16 00:55:22',0),(21,1,'ecdf97ed-113c-44c8-a588-ce3f6df41ee9','access','2022-02-14 01:11:36',0),(22,1,'505063ea-aa40-45da-8de0-88225811c294','refresh','2022-03-16 00:56:36',0),(23,1,'c55fabb8-dc3c-4695-9d4b-ffb830a2e1d6','access','2022-02-14 09:30:21',0),(24,1,'219e9797-8975-4709-8a9b-bb948d118ee6','refresh','2022-03-16 09:15:21',0),(25,1,'18d179b9-7292-4ebb-ba0b-6e894c6a8d99','access','2022-02-14 10:07:28',0),(26,1,'225543a3-fe20-4d58-b2ca-93f06f514a60','refresh','2022-03-16 09:52:28',0),(27,1,'d10a0f1f-ffd7-48fb-80c4-1c8f635ef1b0','access','2022-02-14 10:39:48',0),(28,1,'bb11eb4b-ad30-439f-8467-db00bf5c8f63','refresh','2022-03-16 10:24:48',0),(29,1,'59ffa2d0-dc36-442f-889a-aea22ef34f63','access','2022-02-14 10:45:39',0),(30,1,'72b46379-deca-4984-99fc-65fb82046496','refresh','2022-03-16 10:30:39',0),(31,1,'43b58b06-5273-409d-8abb-70887ec3d1cc','access','2022-02-14 10:51:14',0),(32,1,'ecd6d95a-d7e7-41ed-8d6e-edc73919e7ef','refresh','2022-03-16 10:36:14',0),(33,1,'d1f51429-1847-4409-bd45-84bbd590b98f','access','2022-02-16 09:33:50',0),(34,1,'dc2c6de6-6166-40ee-9a5b-f4ec094a53f9','refresh','2022-03-18 09:18:50',0),(35,1,'98c3e1cf-c73b-465a-96b7-7530f7b67305','access','2022-02-16 16:56:01',0),(36,1,'8f960442-a45d-42fd-8e14-c81b30a2ecc3','refresh','2022-03-18 16:41:01',0),(37,1,'18cd39f1-4d60-4bd3-8299-1760a62438b9','access','2022-02-16 18:21:50',0),(38,1,'2880637a-bf4b-4e33-a4f6-0d2fa26800d1','refresh','2022-03-18 18:06:50',0),(39,1,'2bc2bdaf-3c67-4e1d-b244-4f5e73307f52','access','2022-02-16 18:44:48',0),(40,1,'4a7635da-4695-4570-ad37-a993ae60ab00','refresh','2022-03-18 18:29:48',0),(41,1,'c72e87c3-24ac-4b57-a541-22a6e146617b','access','2022-02-17 11:29:13',0),(42,1,'77559076-2f23-42cf-95b9-3baeaecf2016','refresh','2022-03-19 11:14:13',0),(43,1,'b0809ec1-4051-40fa-84ab-def8881e3443','access','2022-02-17 11:56:47',0),(44,1,'606c8178-4398-457d-8cb4-b07b5d49e195','refresh','2022-03-19 11:41:47',0),(45,1,'270ccc5b-94b3-4c58-9774-ff893621cbec','access','2022-02-17 12:06:18',0),(46,1,'10a55a09-634c-4bb8-bf61-056c2f559a3c','refresh','2022-03-19 11:51:18',0),(47,1,'6d189c94-ca1d-4977-8d33-0a019176781b','access','2022-02-17 13:53:30',0),(48,1,'1f37906d-4402-4cab-8946-5ad236d9bff4','refresh','2022-03-19 13:38:30',0),(49,1,'d600c01d-d4d9-4aaf-93d7-c0d574872390','access','2022-02-19 07:35:58',0),(50,1,'7ebc3da3-5c69-4746-ba2a-9ee73e41fb34','refresh','2022-03-21 07:20:58',0),(51,1,'afb1f30b-05df-463b-b2b0-5eddff18dd23','access','2022-02-19 08:36:27',0),(52,1,'6ce48364-86ab-40fb-befb-4aafc680246a','refresh','2022-03-21 08:21:27',0),(53,1,'2dee9778-03cc-4d5c-822e-ae7f6e0dbbd3','access','2022-02-20 07:16:14',0),(54,1,'c8badf45-625a-4720-936c-2ba67be8ba11','refresh','2022-03-22 07:01:14',0),(55,1,'07ee2569-56d7-4906-8181-5e3dd18dc927','access','2022-02-20 07:43:08',0),(56,1,'cf7f69cd-a60f-4e14-b402-95fbe5bfe4c1','refresh','2022-03-22 07:28:08',0),(57,1,'7325908c-5d2f-49ba-a0c9-4ec4cb21c8be','access','2022-02-20 08:23:32',0),(58,1,'bcf86311-5ed6-4086-a208-67789fdd7c03','refresh','2022-03-22 08:08:32',0),(59,1,'959ed947-cd5b-4032-b102-8e598c81e054','access','2022-02-20 08:46:24',0),(60,1,'2299a1cb-3d5b-4054-9c1f-6caa12961adf','refresh','2022-03-22 08:31:24',0),(61,1,'ea9c0332-48d9-4703-a3d8-667d1684c004','access','2022-02-20 09:32:49',0),(62,1,'f3af4065-4b63-4bfe-ad00-1c1ebe04b8c6','refresh','2022-03-22 09:17:49',0),(63,1,'13fa1ab9-ae0f-41be-80bc-acd131996675','access','2022-02-20 09:33:53',0),(64,1,'55d8e20a-8420-4c85-bff3-9c95d258a996','refresh','2022-03-22 09:18:53',0),(65,1,'3af3ab6b-302e-453e-9e74-f7655cca79b2','access','2022-02-21 08:21:21',0),(66,1,'825ae167-41d1-4214-a4b6-21d3a518be2a','refresh','2022-03-23 08:06:21',0),(67,1,'ad19cf3d-b573-4e77-bb3c-5cca1bce7e06','access','2022-02-21 08:44:13',0),(68,1,'459eb038-6f5e-46a2-80c2-830ea2bafb8e','refresh','2022-03-23 08:29:13',0),(69,1,'3240fafc-f108-4049-b997-befed52ddfff','access','2022-02-21 09:04:20',0),(70,1,'9f2a94c1-5042-4fd3-ad8b-91d156e2fa55','refresh','2022-03-23 08:49:20',0),(71,1,'097d3119-ca11-439e-8fd9-6bb136abde2e','access','2022-02-21 09:20:39',0),(72,1,'e99caae5-189b-4205-9ce1-348f6a5cbfac','refresh','2022-03-23 09:05:39',0),(73,1,'02045603-5fbe-4ee0-b942-55d34b45b97b','access','2022-02-21 10:41:20',0),(74,1,'fce24cfb-1489-4aee-b9cc-eb4f8e32c6d8','refresh','2022-03-23 10:26:20',0),(75,1,'61f03266-0d7d-482c-94ca-3870ae4faa7c','access','2022-02-23 14:43:51',0),(76,1,'56ba0d03-2a06-4bb8-989f-42ea6e288560','refresh','2022-03-25 14:28:51',0),(77,1,'01eaafc5-00e1-4844-93da-3474f87e976d','access','2022-02-23 16:26:48',0),(78,1,'d500382a-62e4-42e1-990d-96917b0e9922','refresh','2022-03-25 16:11:48',0),(79,1,'6653a9bc-36a8-424b-a27e-560866d7c313','access','2022-02-23 16:44:41',0),(80,1,'e2087ecc-0ca4-4c6a-805c-5fefe3ba78df','refresh','2022-03-25 16:29:41',0),(81,1,'3280f10b-1373-4e3f-ab80-ee070753e774','access','2022-02-24 09:19:36',0),(82,1,'fed813f4-fed4-44e3-8d5a-f345de76ffff','refresh','2022-03-26 09:04:36',0),(83,1,'592c65e0-15d6-47ce-a6d5-2eb8002b8dae','access','2022-02-24 09:43:20',0),(84,1,'987b1b38-95d4-4e3c-9aac-bd474e48c1e1','refresh','2022-03-26 09:28:20',0),(85,1,'db805ad0-daa7-4772-b109-0bd7fc4322bc','access','2022-02-24 10:51:35',0),(86,1,'13e45258-b35d-47a9-9273-2311d0b3076e','refresh','2022-03-26 10:36:35',0),(87,1,'e8ba43d8-7724-4972-9fce-c1a4eba61d70','access','2022-02-24 10:54:02',0),(88,1,'522bd8e5-de50-4fc7-817b-27f002965ba9','refresh','2022-03-26 10:39:02',0),(89,1,'4d76e97a-b3e8-43a7-b3d9-4b008ae6534a','access','2022-02-24 11:09:07',0),(90,1,'1dd531f7-7d18-49bd-bc68-447cd0f525af','refresh','2022-03-26 10:54:07',0),(91,1,'8ef46f94-108b-4597-9cc7-31f1ef406e05','access','2022-02-25 12:33:44',0),(92,1,'ebac6990-42c4-4c0b-a6b1-4cf7743bfe42','refresh','2022-03-27 12:18:44',0),(93,1,'5158c6c4-b14d-4305-926e-dd5df41bf138','access','2022-02-28 08:53:06',0),(94,1,'4f484000-4246-48f0-ad9d-3e44dd857206','refresh','2022-03-30 08:38:06',0),(95,1,'11248ab3-5bd0-4f04-b5ae-3c0ea0c116b4','access','2022-02-28 09:24:11',0),(96,1,'fdda7684-4195-49ea-a652-da3a1f01ed85','refresh','2022-03-30 09:09:11',0),(97,1,'6efdfae7-b9a3-466c-a1bd-c8f7e643e1e5','access','2022-02-28 09:36:44',0),(98,1,'a76c0e5e-14bd-419e-a57e-5d7587b929c1','refresh','2022-03-30 09:21:44',0),(99,1,'2a4dd19f-4023-47fa-a5f0-9a863f2dea95','access','2022-02-28 09:38:14',0),(100,1,'31a5f2f5-087a-47de-9782-09a18eddaf02','refresh','2022-03-30 09:23:14',0),(101,1,'dafd07af-59db-44a8-98e4-7cd62ea67a49','access','2022-02-28 09:53:42',0),(102,1,'f37c5638-a3c1-48b7-9b88-634197414e5e','refresh','2022-03-30 09:38:42',0),(103,1,'26cc101c-52e8-4f14-b9cb-9658ab2c4776','access','2022-02-28 09:56:33',0),(104,1,'58402182-dd06-42a7-a3a8-336008420ae8','refresh','2022-03-30 09:41:33',0),(105,1,'1b084da2-8f87-455e-8880-eb20cc0c2ab6','access','2022-02-28 11:20:20',0),(106,1,'c3380c49-fedc-4e32-a0fc-e212c00ef0e0','refresh','2022-03-30 11:05:20',0),(107,1,'0d935717-a4aa-4c69-bf8d-165872373f0c','access','2022-02-28 11:20:33',0),(108,1,'b95997cb-c338-48b8-b1b6-c0cab849edb5','refresh','2022-03-30 11:05:33',0),(109,1,'5f97681e-d102-43a0-a97d-4e702ce30fd3','access','2022-02-28 11:21:09',0),(110,1,'23ead59b-4221-434b-8f3e-eb9ebd823ffd','refresh','2022-03-30 11:06:09',0),(111,1,'78d3e26b-686d-41f8-ade6-22d0645f892b','access','2022-02-28 11:22:47',0),(112,1,'d15daf9e-196a-4e64-b5f9-e16a6913492f','refresh','2022-03-30 11:07:47',0),(113,1,'78ee45b1-8cd4-42c4-a714-b48a8f9b6a10','access','2022-02-28 11:24:51',0),(114,1,'284e1134-1ec8-462d-9502-ec59f91038bf','refresh','2022-03-30 11:09:51',0),(115,1,'860cfe2a-d0be-4d5e-b420-ea2c70b837e6','access','2022-02-28 11:25:01',0),(116,1,'bb1fbe51-dc5a-475d-a64f-d8205a6d6a7f','refresh','2022-03-30 11:10:01',0),(117,1,'35953c62-1f70-4a3f-be67-adcb23fd8f57','access','2022-02-28 11:38:37',0),(118,1,'3fb7cd3e-86e6-4ba3-aac7-0d9b61a6c57d','refresh','2022-03-30 11:23:37',0),(119,1,'0ef00e51-8ffe-42a6-a92a-bfd8c6d24289','access','2022-02-28 11:38:53',0),(120,1,'cdd2dbad-a25e-4eda-a69f-e455b0bf0c2a','refresh','2022-03-30 11:23:53',0),(121,1,'5aed5d12-fd50-44fe-9f64-e019246f8e3b','access','2022-02-28 11:40:50',0),(122,1,'6ed38d50-44aa-4761-bcc7-c6772e52a1b6','refresh','2022-03-30 11:25:50',0),(123,1,'84cec1d2-1b5b-4dd0-8e49-bfcf9124c5cc','access','2022-02-28 11:41:05',0),(124,1,'7b32f4bb-7790-4e2d-ad64-0e5bd93d6bc4','refresh','2022-03-30 11:26:05',0),(125,1,'86848b01-1000-40df-8ce1-070cb9cfcd0f','access','2022-02-28 23:11:10',0),(126,1,'7c7d7180-cacb-4eed-afce-2422be41f8c2','refresh','2022-03-30 22:56:10',0),(127,1,'54519c97-67e7-497b-8971-2b6ad9c281b7','access','2022-02-28 23:22:56',0),(128,1,'9d6ad8ac-0f78-4e21-9c85-6b2cd82bd5e8','refresh','2022-03-30 23:07:56',0),(129,1,'cc9ee387-07a4-4852-ad39-23ad8acf4886','access','2022-02-28 23:30:35',0),(130,1,'34b08518-4e62-4a8a-82a8-319cbdf921e0','refresh','2022-03-30 23:15:35',0),(131,1,'0bcef308-0e65-4ff0-974c-8982fe14e865','access','2022-02-28 23:41:27',0),(132,1,'1b83cb02-31ea-4fc7-8ab3-7e2665958458','refresh','2022-03-30 23:26:27',0),(133,1,'7888dac2-26e9-4306-9198-eeec19ea8c99','access','2022-03-01 00:01:52',0),(134,1,'5c5a1d4d-396d-4783-a883-c70901cb2d01','refresh','2022-03-30 23:46:52',0),(135,1,'ba97c418-5b97-41e4-a838-5d9e472fde40','access','2022-03-01 00:02:08',0),(136,1,'123bdc0d-432b-46cf-aa9b-871b9a0ad58f','refresh','2022-03-30 23:47:08',0),(137,1,'1a6ac50d-fb7a-4e3c-a5be-31a62bb31520','access','2022-03-01 00:06:25',0),(138,1,'47a21358-2dd9-4ca6-8360-7a968b3f44f3','refresh','2022-03-30 23:51:25',0),(139,1,'5a7c31b0-04d5-4204-91f9-bb25c2ad5f03','access','2022-03-01 00:06:49',0),(140,1,'154daf4a-0787-4fa1-8762-8ccbd8474a7b','refresh','2022-03-30 23:51:49',0),(141,1,'0b41ce86-a8bc-4d92-8508-7f379d87dd47','access','2022-03-01 00:08:33',0),(142,1,'cbcd4190-8baa-4218-925a-fb76b6fe3202','refresh','2022-03-30 23:53:33',0),(143,1,'28ff6047-5369-4bd0-8484-7e3015855593','access','2022-03-07 21:58:11',0),(144,1,'a0f86b1d-fca8-4f6c-ab65-ac2ff9770c82','refresh','2022-04-06 21:43:11',0),(145,1,'84f2894e-f6ec-4f57-917a-d23da1daa4c6','access','2022-03-07 22:20:42',0),(146,1,'06ceab4d-2673-4273-bded-eedb2a680b0a','refresh','2022-04-06 22:05:42',0),(147,1,'9b4d8eb5-c80e-415c-9735-c315264b9af0','access','2022-03-07 22:24:00',0),(148,1,'caf1e221-7193-4ec3-88ae-f7d3ad388530','refresh','2022-04-06 22:09:00',0),(149,1,'e703ccbf-d269-4d7b-a20b-386ea5345661','access','2022-03-07 22:26:48',0),(150,1,'250c0384-2d03-467d-94ff-522b493b8f4d','refresh','2022-04-06 22:11:48',0),(151,1,'0232713d-4d54-4d36-8e59-e4b047f6bf06','access','2022-03-07 22:33:05',0),(152,1,'68dde1c7-2566-4d49-a51c-cc040706b48d','refresh','2022-04-06 22:18:05',0),(153,1,'cc281221-3b7b-436a-b4e0-c08ae7078dd7','access','2022-03-07 22:35:47',0),(154,1,'7a55bcda-d58d-43bd-843c-df02d08ed72c','refresh','2022-04-06 22:20:47',0),(155,1,'35d4903f-0dd5-4e7c-9b3c-3637130993c1','access','2022-03-07 22:35:47',0),(156,1,'31905297-994e-48d3-97b7-0ec171c3fcc9','access','2022-03-07 22:35:47',0),(157,1,'e4650bd1-9883-446c-a312-39058eae568f','refresh','2022-04-06 22:20:47',0),(158,1,'420d21aa-ac38-440f-9e08-58d35854e9c1','refresh','2022-04-06 22:20:47',0),(159,1,'a7607526-d73c-4ea2-9e3f-3ed194f9acc5','access','2022-03-08 10:01:45',0),(160,1,'2c966cdd-6a02-43f1-b280-6b3522d421c2','refresh','2022-04-07 09:46:45',0),(161,1,'16a48097-9cbb-4c31-b3f1-02e10a156f8e','access','2022-03-09 08:46:51',0),(162,1,'0783d753-6023-4cac-a091-da7224e302b6','refresh','2022-04-08 08:31:51',0),(163,1,'b28d1304-e5e7-40ca-ad65-5944c407241b','access','2022-03-09 09:09:42',0),(164,1,'9efb702b-e661-48a1-96c5-8c01c398abbe','refresh','2022-04-08 08:54:42',0),(165,1,'4c1a9a90-abd7-45e9-8dd3-55644e3fb68b','access','2022-03-09 09:13:03',0),(166,1,'6abf3db2-a222-4366-b030-50e3ea614d4e','refresh','2022-04-08 08:58:03',0),(167,1,'e1191522-c601-4f12-ab56-a7e25b0c2782','access','2022-03-09 09:13:50',0),(168,1,'00ee1617-4fa8-42a5-943d-6e9f7706eedd','refresh','2022-04-08 08:58:50',0),(169,1,'b5d994b9-e87f-42d9-916b-5c781053d7ec','access','2022-03-09 09:14:30',0),(170,1,'3599e856-17ac-4835-9815-d5d8c918d816','refresh','2022-04-08 08:59:30',0),(171,1,'09bbf9a5-bed0-400f-8990-d6db3e7d0445','access','2022-03-09 09:16:01',0),(172,1,'3d8e8aa1-14a4-4165-9cbc-1cd578fbc3df','refresh','2022-04-08 09:01:01',0),(173,1,'34a8de2f-d8f1-4ecd-83b4-29928ed3ef4b','access','2022-03-09 09:25:59',0),(174,1,'c2b58c05-3e60-4529-a955-c4aa2e8b6b74','refresh','2022-04-08 09:10:59',0),(175,1,'972f3578-0cad-402b-9b51-b485b3f70910','access','2022-03-09 09:28:20',0),(176,1,'1c58e765-29b0-4a7c-bf87-122fdadd5083','refresh','2022-04-08 09:13:20',0),(177,1,'8297743d-2203-48e4-b352-040228619043','access','2022-03-09 09:29:23',0),(178,1,'8d055ebf-751e-42c1-81a3-3ab753beba41','refresh','2022-04-08 09:14:23',0),(179,1,'546a6611-e7ca-4f8f-8eb4-704e11c2557e','access','2022-03-09 09:31:35',0),(180,1,'2c97d72c-5d10-43b3-bf67-f6a8066d752a','refresh','2022-04-08 09:16:35',0),(181,1,'4d2fffc2-e3b4-401a-982c-88e483e240df','access','2022-03-09 09:32:30',0),(182,1,'59183ca0-ecc2-4228-bb56-a366857b824e','refresh','2022-04-08 09:17:30',0),(183,1,'2c909abf-4431-48f2-8bc4-197254583342','access','2022-03-09 09:34:00',0),(184,1,'154bce47-c4f4-44c4-972b-101cb7866426','refresh','2022-04-08 09:19:00',0),(185,1,'89d483e0-8ea4-4bf6-a494-6475cb2a4e33','access','2022-03-09 09:41:19',0),(186,1,'87d0ff35-2cb7-4ff1-b25c-a97cf5532c46','refresh','2022-04-08 09:26:19',0),(187,1,'a05731e5-8a56-4c8d-a45b-bcc3ec9418e2','access','2022-03-09 09:50:02',0),(188,1,'ee793a0a-b96e-4636-8b44-86f9c9e17d15','refresh','2022-04-08 09:35:02',0),(189,1,'fcc1267b-8822-4432-87f9-0e9c6dbee554','access','2022-03-09 10:02:17',0),(190,1,'c579374e-212b-4ff2-86ef-a720ef250d20','refresh','2022-04-08 09:47:17',0),(191,1,'97636256-f3fe-4930-b0d3-adfa4bf48f6d','access','2022-03-09 10:03:52',0),(192,1,'571714aa-bdab-4370-ad75-cb8904de5fed','refresh','2022-04-08 09:48:52',0),(193,1,'ca124373-4fcc-43a2-9027-c369e1b46855','access','2022-03-09 10:09:09',0),(194,1,'d847815c-1d44-4b92-9ff1-ef57cd8122dd','refresh','2022-04-08 09:54:09',0),(195,1,'e6a265c2-e124-4ffe-914e-58c13bf18147','access','2022-03-09 10:31:24',0),(196,1,'6a15131a-f43d-4237-bd65-aa54f0d631a8','refresh','2022-04-08 10:16:24',0),(197,1,'df713546-3366-421b-b2ca-6b2b7e3dfd09','access','2022-03-09 10:33:38',0),(198,1,'b39f31eb-aa43-472b-a22f-f8f49c9c57d1','refresh','2022-04-08 10:18:38',0),(199,1,'80e47495-33b5-413a-8e80-d3d5afcfa45e','access','2022-03-09 10:34:33',0),(200,1,'0fbfeb7b-2bbb-4542-b538-061b5042d3dc','refresh','2022-04-08 10:19:33',0),(201,1,'807781f4-bd69-457d-b4b0-dbb53d34c648','access','2022-03-09 10:37:18',0),(202,1,'461f6760-4647-42ad-8945-5b7630c4174b','refresh','2022-04-08 10:22:18',0),(203,1,'4bb93972-7359-4be1-813d-1e85034a577d','access','2022-03-09 11:39:46',0),(204,1,'81ea232c-f50a-4f8b-8628-f296357fc9dc','refresh','2022-04-08 11:24:46',0),(205,1,'714dc1bf-ad5f-41d1-97d9-ca5b893af3c6','access','2022-03-09 11:41:11',0),(206,1,'4863375e-dab4-4de9-9091-e76fa6d59f52','refresh','2022-04-08 11:26:11',0),(207,1,'3b7bcba3-7b1b-4959-a137-5ddc45d9be51','access','2022-03-09 12:36:09',0),(208,1,'5e6512f2-ce31-4c06-95ef-a878f679d4e2','refresh','2022-04-08 12:21:09',0),(209,1,'51a31c47-7183-4c19-bdf9-37d1d06e1753','access','2022-03-09 12:36:25',0),(210,1,'f1d9f325-4007-4eec-b944-d6773675a1fb','refresh','2022-04-08 12:21:25',0),(211,1,'b117a010-9a74-4635-84d5-95eb00322b0b','access','2022-03-09 12:38:06',0),(212,1,'50a6dbc0-8aff-4f78-8ad8-fc2bc049ae65','refresh','2022-04-08 12:23:06',0),(213,1,'7f54049e-7d56-485f-8e81-ab03492aabb1','access','2022-03-09 12:40:04',0),(214,1,'e938273e-32f8-45ca-8020-c930c6429035','refresh','2022-04-08 12:25:04',0),(215,1,'8570c8e9-7d88-4629-9a26-2be2e12a432d','access','2022-03-09 12:42:04',0),(216,1,'936b9077-81a2-4071-a8c8-17ea3a4b2752','refresh','2022-04-08 12:27:04',0),(217,1,'4db08c90-6dcf-426b-8656-f931bd4f1db5','access','2022-03-09 12:43:55',0),(218,1,'0e039777-ecb7-4c6a-bc24-38961f7f8c6b','refresh','2022-04-08 12:28:55',0),(219,1,'4c803970-4186-47a8-aa54-85751f220506','access','2022-03-09 12:44:33',0),(220,1,'ba2284cb-dfce-4a3b-a3d2-7db4923d35db','refresh','2022-04-08 12:29:33',0),(221,1,'93002506-b63a-419a-9090-1931e65e3fd8','access','2022-03-09 12:47:18',0),(222,1,'ca8a5aa1-7a13-4537-bc4b-b911fba7c0dd','refresh','2022-04-08 12:32:18',0),(223,1,'f570fc8f-c809-48c9-8a56-0d97ef20eba5','access','2022-03-09 12:49:21',0),(224,1,'623479ce-d5a3-490e-9699-3aecbc620cd4','refresh','2022-04-08 12:34:21',0),(225,1,'7512d031-6e4f-4147-a467-0a14dca3c501','access','2022-03-09 12:50:14',0),(226,1,'83e23ef0-ad41-4113-99e5-6c0d8bae40d0','refresh','2022-04-08 12:35:14',0),(227,1,'ce85b509-fb1d-44ed-9de6-4e5304a360c6','access','2022-03-09 12:51:28',0),(228,1,'900a6255-42f9-4973-b7e4-208325ca3032','refresh','2022-04-08 12:36:28',0),(229,1,'86048188-0167-4beb-8052-51d57422b1f1','access','2022-03-09 12:51:58',0),(230,1,'548738e3-c67c-4ac6-a74c-202b5c2d887a','refresh','2022-04-08 12:36:58',0),(231,1,'4a335d9e-c0d8-4bd7-9ef6-146f99b8e734','access','2022-03-09 12:52:20',0),(232,1,'6d9964d4-fcd6-4146-8f60-95c9c996deff','refresh','2022-04-08 12:37:20',0),(233,1,'28affa8a-fef3-4f9f-ae37-b9502dc168bf','access','2022-03-09 12:53:24',0),(234,1,'50d9646a-0a47-4b2a-a2d3-3a07403a8969','refresh','2022-04-08 12:38:24',0),(235,1,'63bd13d3-188e-49d5-870f-a70f410451c4','access','2022-03-09 12:53:36',0),(236,1,'b2d23498-bd1c-4c9d-bf3d-70b8eb9550a3','refresh','2022-04-08 12:38:36',0),(237,1,'66db8de1-4208-4df1-bfdf-25af3dae1c10','access','2022-03-09 12:54:01',0),(238,1,'25a00df2-7a65-4ebd-89b2-d874b6bd16a4','refresh','2022-04-08 12:39:01',0),(239,1,'88e5a281-2219-4fa5-9c70-c70aa48e457a','access','2022-03-09 12:56:06',0),(240,1,'2b450416-9034-42f2-9518-7a929192974a','refresh','2022-04-08 12:41:06',0),(241,1,'9168c644-0c50-48e9-b126-cd269d49af75','access','2022-03-09 12:58:08',0),(242,1,'c8070f14-eeef-4858-ac6b-35acee4909ff','refresh','2022-04-08 12:43:08',0),(243,1,'b55df9ca-a135-453e-afc2-9678c656faf1','access','2022-03-09 12:58:37',0),(244,1,'f242b2d0-31c2-4150-827c-942987aeaeeb','refresh','2022-04-08 12:43:37',0),(245,1,'5188555b-6347-4c36-afa4-9a055b58573e','access','2022-03-09 12:59:23',0),(246,1,'d08efb31-1f9a-441a-9f40-7cbd34f39f39','refresh','2022-04-08 12:44:23',0),(247,1,'2affe83e-0379-4afa-bea1-d22fc0c2ca11','access','2022-03-09 12:59:56',0),(248,1,'ecfc8ff7-88e3-4623-ab59-9cccc85e57e5','refresh','2022-04-08 12:44:56',0),(249,1,'cedb507d-01d0-43a4-b4cd-fbdcf2f5841a','access','2022-03-09 13:59:33',0),(250,1,'20f28eea-8d17-4e79-ae98-beb68e12c71c','refresh','2022-04-08 13:44:33',0),(251,1,'1b405f8b-a2b5-4b4b-9bcc-463dd78dea8d','access','2022-03-09 14:12:03',0),(252,1,'e81347cc-042b-4c81-827a-fc4add34f22f','refresh','2022-04-08 13:57:03',0),(253,1,'aa0d9447-c33b-4743-9a8f-e6c576e46b9a','access','2022-03-09 14:25:40',0),(254,1,'2343a964-57a6-456f-b571-beff5c7505d8','refresh','2022-04-08 14:10:40',0),(255,1,'010fdd68-d57a-484a-bf0b-51c2b59739e1','access','2022-03-09 14:38:24',0),(256,1,'83e013e3-7dac-40c4-a257-64c8200f14c4','refresh','2022-04-08 14:23:24',0),(257,1,'9b0c71c5-3478-479b-8eae-6fbf0893ab56','access','2022-03-09 14:40:15',0),(258,1,'e91f06dc-21b5-4901-ad4a-50dad4bcaf72','refresh','2022-04-08 14:25:15',0),(259,1,'105b427a-f1a6-4177-9396-26b66cb11db2','access','2022-03-09 14:47:45',0),(260,1,'9a68a9d3-cdce-4063-a292-e2607d7d5e2b','refresh','2022-04-08 14:32:45',0),(261,1,'c2f98784-59e8-4cb4-9fd7-d8869bf83745','access','2022-03-09 14:49:20',0),(262,1,'3de05e4c-591d-443d-9ccb-43103e737b26','refresh','2022-04-08 14:34:20',0),(263,1,'8f375d51-7664-46aa-b390-644657d8948e','access','2022-03-09 14:50:12',0),(264,1,'98b32a4c-8960-40d4-b89f-83eb1a85863d','refresh','2022-04-08 14:35:12',0),(265,1,'66a5f683-625a-41a4-ac9e-cd498e0a79c2','access','2022-03-09 14:54:11',0),(266,1,'e8ff3163-6664-4a3e-b012-b14fb632209f','refresh','2022-04-08 14:39:11',0);
/*!40000 ALTER TABLE `api_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id_entidad` int NOT NULL AUTO_INCREMENT,
  `razon_social` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `nit_ci` varchar(31) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_entidad`),
  UNIQUE KEY `id_cliente_UNIQUE` (`id_entidad`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'barron','1280420','mnik','2022-02-07 08:44:17',1),(2,'test_2','123456010','dev','2022-02-20 09:19:43',1),(4,'moralejas','123456789','dev','2022-02-07 23:19:41',0),(8,'test_upd','123456010_upd','dev','2022-02-14 00:50:18',0);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `id_compra` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_proveedor` int NOT NULL,
  `monto_total` decimal(10,2) NOT NULL,
  `fecha` datetime NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_compra`),
  UNIQUE KEY `id_compra_producto_UNIQUE` (`id_compra`),
  KEY `id_usuario_idx` (`id_usuario`),
  KEY `id_proveedor_idx` (`id_proveedor`),
  CONSTRAINT `id_proveedor` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id_entidad`),
  CONSTRAINT `id_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_entidad`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (3,1,6,10.00,'2022-02-22 08:31:00','dev','2022-02-24 09:08:25',1),(4,1,6,20.00,'2020-02-21 08:48:00','dev','2022-02-24 09:30:04',1),(5,1,6,2000.00,'2020-02-21 08:48:00','dev','2022-02-24 09:30:38',0);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacto`
--

DROP TABLE IF EXISTS `contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacto` (
  `id_contacto` int NOT NULL AUTO_INCREMENT,
  `id_entidad` int NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_contacto`),
  UNIQUE KEY `id_contacto_UNIQUE` (`id_contacto`),
  KEY `id_entidad_ibfk_idx` (`id_entidad`),
  CONSTRAINT `id_entidad_ibfk` FOREIGN KEY (`id_entidad`) REFERENCES `entidad` (`id_entidad`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto`
--

LOCK TABLES `contacto` WRITE;
/*!40000 ALTER TABLE `contacto` DISABLE KEYS */;
INSERT INTO `contacto` VALUES (1,1,'2022-02-16 18:07:18','dev',1),(2,2,'2022-02-16 18:08:01','dev',0);
/*!40000 ALTER TABLE `contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacto_correo`
--

DROP TABLE IF EXISTS `contacto_correo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacto_correo` (
  `id_contacto_correo` int NOT NULL AUTO_INCREMENT,
  `id_contacto` int NOT NULL,
  `correo` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_contacto_correo`),
  UNIQUE KEY `id_contacto_correo_UNIQUE` (`id_contacto_correo`),
  KEY `id_contacto_ibfk_idx` (`id_contacto`),
  CONSTRAINT `id_contacto_ibfk` FOREIGN KEY (`id_contacto`) REFERENCES `contacto` (`id_contacto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto_correo`
--

LOCK TABLES `contacto_correo` WRITE;
/*!40000 ALTER TABLE `contacto_correo` DISABLE KEYS */;
INSERT INTO `contacto_correo` VALUES (1,1,'test222@testmail.com','dev','2022-02-17 11:14:49',1),(2,1,'test_upd@testmail.com','dev','2022-02-17 11:15:53',0);
/*!40000 ALTER TABLE `contacto_correo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacto_direccion`
--

DROP TABLE IF EXISTS `contacto_direccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacto_direccion` (
  `id_contacto_direccion` int NOT NULL AUTO_INCREMENT,
  `id_contacto` int NOT NULL,
  `id_localidad` int NOT NULL,
  `calle` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `numero_casa` varchar(31) COLLATE utf8_spanish_ci NOT NULL,
  `zona` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `detalles` varchar(1024) COLLATE utf8_spanish_ci DEFAULT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_contacto_direccion`),
  KEY `id_contacto` (`id_contacto`),
  KEY `id_localidad_ibfk_idx` (`id_localidad`),
  CONSTRAINT `id_contacto_2` FOREIGN KEY (`id_contacto`) REFERENCES `contacto` (`id_contacto`),
  CONSTRAINT `id_localidad_ibfk` FOREIGN KEY (`id_localidad`) REFERENCES `localidad` (`id_localidad`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto_direccion`
--

LOCK TABLES `contacto_direccion` WRITE;
/*!40000 ALTER TABLE `contacto_direccion` DISABLE KEYS */;
INSERT INTO `contacto_direccion` VALUES (1,1,1,'real st.','5','surapata','a la vuelta de las graditas','dev','2022-02-17 13:41:39',1),(2,1,1,'realest st. upd','5','surapata','a la vuelta de las graditas','dev','2022-02-17 13:43:39',0);
/*!40000 ALTER TABLE `contacto_direccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacto_telefono`
--

DROP TABLE IF EXISTS `contacto_telefono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacto_telefono` (
  `id_contacto_telefono` int NOT NULL AUTO_INCREMENT,
  `id_contacto` int NOT NULL,
  `codigo_pais` varchar(7) COLLATE utf8_spanish_ci NOT NULL,
  `numero` varchar(31) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_contacto_telefono`),
  UNIQUE KEY `id_contacto_telefono_UNIQUE` (`id_contacto_telefono`),
  KEY `id_contacto_3_idx` (`id_contacto`),
  CONSTRAINT `id_contacto_3` FOREIGN KEY (`id_contacto`) REFERENCES `contacto` (`id_contacto`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto_telefono`
--

LOCK TABLES `contacto_telefono` WRITE;
/*!40000 ALTER TABLE `contacto_telefono` DISABLE KEYS */;
INSERT INTO `contacto_telefono` VALUES (1,1,'+591','64-60000','dev','2022-02-17 11:44:11',1),(2,1,'+upd','64-60001-upd','dev','2022-02-17 11:47:55',1),(3,1,'+591','64-60001','dev','2022-02-17 11:50:01',0);
/*!40000 ALTER TABLE `contacto_telefono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `id_departamento` int NOT NULL AUTO_INCREMENT,
  `nombre_departamento` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_departamento`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Beni'),(2,'Chuquisaca'),(3,'La Paz'),(4,'Oruro'),(5,'Pando'),(6,'Potosí'),(7,'Santa Cruz'),(8,'Tarija'),(9,'Cochabamba');
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_entrada`
--

DROP TABLE IF EXISTS `detalle_entrada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_entrada` (
  `id_detalle_entrada` int NOT NULL AUTO_INCREMENT,
  `id_compra` int NOT NULL,
  `id_producto` int NOT NULL,
  `cantidad` int NOT NULL,
  `precio_unidad` decimal(10,2) NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_detalle_entrada`),
  UNIQUE KEY `id_detalle_entrada_UNIQUE` (`id_detalle_entrada`),
  KEY `id_compra_producto_ibfk_idx` (`id_compra`),
  KEY `id_producto_ibfk_idx` (`id_producto`),
  CONSTRAINT `id_compra_producto_ibfk` FOREIGN KEY (`id_compra`) REFERENCES `compra` (`id_compra`),
  CONSTRAINT `id_producto_ibfk` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_entrada`
--

LOCK TABLES `detalle_entrada` WRITE;
/*!40000 ALTER TABLE `detalle_entrada` DISABLE KEYS */;
INSERT INTO `detalle_entrada` VALUES (6,3,1,1,1.80,'dev','2022-02-24 09:13:54',1),(7,3,1,13,3.90,'dev','2022-02-24 09:14:18',0);
/*!40000 ALTER TABLE `detalle_entrada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_salida`
--

DROP TABLE IF EXISTS `detalle_salida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_salida` (
  `id_detalle_salida` int NOT NULL AUTO_INCREMENT,
  `id_salida_producto` int NOT NULL,
  `id_producto` int NOT NULL,
  `cantidad` varchar(45) COLLATE utf8_spanish_ci NOT NULL,
  `precio_unidad` decimal(10,2) NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_detalle_salida`),
  UNIQUE KEY `id_detalle_salida_UNIQUE` (`id_detalle_salida`),
  KEY `id_salida_producto_idx` (`id_salida_producto`),
  KEY `id_producto_ibfk_idx` (`id_producto`),
  KEY `id_producto_ibfk_2_idx` (`id_producto`),
  CONSTRAINT `id_producto_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`),
  CONSTRAINT `id_salida_producto` FOREIGN KEY (`id_salida_producto`) REFERENCES `salida_producto` (`id_salida_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_salida`
--

LOCK TABLES `detalle_salida` WRITE;
/*!40000 ALTER TABLE `detalle_salida` DISABLE KEYS */;
INSERT INTO `detalle_salida` VALUES (1,3,1,'1',2.00,'dev','2022-02-23 16:12:32',1),(2,3,1,'1',13.80,'dev','2022-02-23 16:12:56',1),(3,3,1,'1',1.80,'dev','2022-02-23 16:13:48',0);
/*!40000 ALTER TABLE `detalle_salida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disposicion`
--

DROP TABLE IF EXISTS `disposicion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disposicion` (
  `id_salida_producto` int NOT NULL,
  `id_usuario` int NOT NULL,
  `id_motivo` int NOT NULL,
  `comentario` varchar(2550) COLLATE utf8_spanish_ci DEFAULT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_salida_producto`),
  UNIQUE KEY `id_disposicion_UNIQUE` (`id_salida_producto`),
  KEY `id_usuario_ibfk_2_idx` (`id_usuario`),
  KEY `id_motivo_ibfk_idx` (`id_motivo`),
  CONSTRAINT `id_motivo_ibfk` FOREIGN KEY (`id_motivo`) REFERENCES `motivo` (`id_motivo`),
  CONSTRAINT `id_salida_producto_pk` FOREIGN KEY (`id_salida_producto`) REFERENCES `salida_producto` (`id_salida_producto`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `id_usuario_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_entidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disposicion`
--

LOCK TABLES `disposicion` WRITE;
/*!40000 ALTER TABLE `disposicion` DISABLE KEYS */;
INSERT INTO `disposicion` VALUES (1,1,1,'test','dev','2022-02-21 08:14:34',1),(2,1,1,'test nueva disposicion updated','dev','2022-02-21 08:15:44',0);
/*!40000 ALTER TABLE `disposicion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entidad`
--

DROP TABLE IF EXISTS `entidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entidad` (
  `id_entidad` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_entidad`),
  UNIQUE KEY `id_entidad_UNIQUE` (`id_entidad`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entidad`
--

LOCK TABLES `entidad` WRITE;
/*!40000 ALTER TABLE `entidad` DISABLE KEYS */;
INSERT INTO `entidad` VALUES (1),(2),(3),(4),(5),(6),(7),(8);
/*!40000 ALTER TABLE `entidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `id_factura` int NOT NULL AUTO_INCREMENT,
  `codigo_control` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `datos_codigo_QR` varchar(1000) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_factura`),
  UNIQUE KEY `id_factura_UNIQUE` (`id_factura`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (1,'adasdasd','asdsadsad','dev','2022-02-21 08:46:28',1),(2,'2022','not available_upd','dev','2022-02-25 12:20:45',0);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `localidad`
--

DROP TABLE IF EXISTS `localidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `localidad` (
  `id_localidad` int NOT NULL AUTO_INCREMENT,
  `id_departamento` int NOT NULL,
  `nombre_localidad` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_localidad`),
  UNIQUE KEY `id_localidad_UNIQUE` (`id_localidad`),
  KEY `id_departamento_ibfk_idx` (`id_departamento`),
  CONSTRAINT `id_departamento_ibfk` FOREIGN KEY (`id_departamento`) REFERENCES `departamento` (`id_departamento`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localidad`
--

LOCK TABLES `localidad` WRITE;
/*!40000 ALTER TABLE `localidad` DISABLE KEYS */;
INSERT INTO `localidad` VALUES (1,2,'Sucre','dev','2022-02-14 10:27:05',1),(2,2,'Sucre','dev','2022-02-14 10:31:20',0);
/*!40000 ALTER TABLE `localidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `motivo`
--

DROP TABLE IF EXISTS `motivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `motivo` (
  `id_motivo` int NOT NULL AUTO_INCREMENT,
  `descripcion_motivo` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_motivo`),
  UNIQUE KEY `id_motivo_UNIQUE` (`id_motivo`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motivo`
--

LOCK TABLES `motivo` WRITE;
/*!40000 ALTER TABLE `motivo` DISABLE KEYS */;
INSERT INTO `motivo` VALUES (1,'Vencimiento','dev','2022-02-21 08:04:09',1),(2,'vencimiento_upd','dev','2022-02-21 08:29:41',0),(3,'Ejemplo_upd','dev','2022-02-28 23:15:46',0),(4,'Ejemplo','dev','2022-02-28 23:47:25',1),(5,'ejemplazo','nadie','2022-03-07 22:18:09',1),(6,'probandoGUI5','dev','2022-03-09 09:35:30',0),(7,'otra prueba','dev','2022-03-09 09:49:10',0),(8,'lol','dev','2022-03-09 09:54:14',0);
/*!40000 ALTER TABLE `motivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nivel`
--

DROP TABLE IF EXISTS `nivel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nivel` (
  `id_nivel` int NOT NULL AUTO_INCREMENT,
  `nivel` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id_nivel`),
  UNIQUE KEY `id_nivel_UNIQUE` (`id_nivel`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nivel`
--

LOCK TABLES `nivel` WRITE;
/*!40000 ALTER TABLE `nivel` DISABLE KEYS */;
INSERT INTO `nivel` VALUES (1,'Administrador'),(2,'Cajero');
/*!40000 ALTER TABLE `nivel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presentacion_producto`
--

DROP TABLE IF EXISTS `presentacion_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `presentacion_producto` (
  `id_presentacion_producto` int NOT NULL AUTO_INCREMENT,
  `id_unidad_presentacion` int NOT NULL,
  `nombre_presentacion` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_presentacion_producto`),
  UNIQUE KEY `id_presentacion_producto_UNIQUE` (`id_presentacion_producto`),
  KEY `id_unidad_presentacion_idx` (`id_unidad_presentacion`),
  CONSTRAINT `id_unidad_presentacion` FOREIGN KEY (`id_unidad_presentacion`) REFERENCES `unidad_presentacion` (`id_unidad_presentacion`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presentacion_producto`
--

LOCK TABLES `presentacion_producto` WRITE;
/*!40000 ALTER TABLE `presentacion_producto` DISABLE KEYS */;
INSERT INTO `presentacion_producto` VALUES (1,1,'frasco','dev','2022-02-19 08:25:25',1),(2,1,'envase_upd','dev','2022-02-19 08:25:40',0);
/*!40000 ALTER TABLE `presentacion_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `id_presentacion_producto` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `codigo` varchar(31) COLLATE utf8_spanish_ci NOT NULL,
  `precio_compra` decimal(10,2) NOT NULL,
  `precio_venta` decimal(10,2) NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_producto`),
  UNIQUE KEY `id_producto_UNIQUE` (`id_producto`),
  KEY `id_presentacion_ibfk_idx` (`id_presentacion_producto`),
  CONSTRAINT `id_presentacion_ibfk` FOREIGN KEY (`id_presentacion_producto`) REFERENCES `presentacion_producto` (`id_presentacion_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,1,'cafe','00001',0.00,0.00,'dev','2022-02-20 07:06:09',1),(2,1,'todys','00002',0.00,0.00,'dev','2022-02-20 07:06:38',0);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_almacen`
--

DROP TABLE IF EXISTS `producto_almacen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_almacen` (
  `id_producto_almacen` int NOT NULL AUTO_INCREMENT,
  `id_almacen` int NOT NULL,
  `id_producto` int NOT NULL,
  `stock_actual` int NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_producto_almacen`),
  UNIQUE KEY `id_producto_almacen_UNIQUE` (`id_producto_almacen`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_almacen`
--

LOCK TABLES `producto_almacen` WRITE;
/*!40000 ALTER TABLE `producto_almacen` DISABLE KEYS */;
INSERT INTO `producto_almacen` VALUES (1,1,1,10,'dev','2022-02-20 08:32:09',1),(2,1,2,5,'dev','2022-02-20 08:32:18',0);
/*!40000 ALTER TABLE `producto_almacen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id_entidad` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_entidad`),
  UNIQUE KEY `id_proveedor_UNIQUE` (`id_entidad`),
  CONSTRAINT `id_entidad_ibfk_2` FOREIGN KEY (`id_entidad`) REFERENCES `entidad` (`id_entidad`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (6,'le proveitor','dev','2022-02-11 00:08:10',1),(7,'actualizado por api','dev','2022-02-11 00:19:48',0);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salida_producto`
--

DROP TABLE IF EXISTS `salida_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salida_producto` (
  `id_salida_producto` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_salida_producto`),
  UNIQUE KEY `id_salida_producto_UNIQUE` (`id_salida_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salida_producto`
--

LOCK TABLES `salida_producto` WRITE;
/*!40000 ALTER TABLE `salida_producto` DISABLE KEYS */;
INSERT INTO `salida_producto` VALUES (1),(2),(3);
/*!40000 ALTER TABLE `salida_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unidad_presentacion`
--

DROP TABLE IF EXISTS `unidad_presentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidad_presentacion` (
  `id_unidad_presentacion` int NOT NULL AUTO_INCREMENT,
  `nombre_medida` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `multiplicador_kg` double NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_unidad_presentacion`),
  UNIQUE KEY `id_unidad_presentacion_UNIQUE` (`id_unidad_presentacion`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidad_presentacion`
--

LOCK TABLES `unidad_presentacion` WRITE;
/*!40000 ALTER TABLE `unidad_presentacion` DISABLE KEYS */;
INSERT INTO `unidad_presentacion` VALUES (1,'frasco de 200g',0.2,'dev','2022-02-19 07:22:29',1),(2,'prueba_upd',0.1,'dev','2022-02-19 07:23:28',0);
/*!40000 ALTER TABLE `unidad_presentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_entidad` int NOT NULL AUTO_INCREMENT,
  `id_nivel` int NOT NULL,
  `login_usuario` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `password_usuario` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_entidad`),
  UNIQUE KEY `id_usuario_UNIQUE` (`id_entidad`),
  KEY `id_nivel_ibfk_idx` (`id_nivel`),
  CONSTRAINT `id_entidad_ibfk_3` FOREIGN KEY (`id_entidad`) REFERENCES `entidad` (`id_entidad`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `id_nivel_ibfk` FOREIGN KEY (`id_nivel`) REFERENCES `nivel` (`id_nivel`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,1,'admin','$pbkdf2-sha256$29000$47w3ZiwF4Nw7RwjhfC.l1A$pCyNmRHMVoCfCcVf4M0E1LEVpQli.Gwb3onzMSoSzZw','dev','2022-02-07 21:30:09',1),(2,2,'cajero','cajero','dev','2022-02-07 21:36:12',1),(3,2,'prueba','prueba','dev','2022-02-07 21:36:29',0),(5,1,'test_api_upd','$pbkdf2-sha256$29000$Q8jZe4.Rcq6VsjZGaC3lnA$yJ.HPlr/GXyPn.ob9.x2A8S5r7lUbUTiXXZ6oaCCuR8','dev','2022-02-10 23:33:14',1);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `id_salida_producto` int NOT NULL,
  `id_usuario` int NOT NULL,
  `id_cliente` int NOT NULL,
  `id_factura` int NOT NULL,
  `fecha` datetime NOT NULL,
  `monto_total` decimal(10,2) NOT NULL,
  `usuario_registro` varchar(127) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `es_registro_activo` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_salida_producto`),
  UNIQUE KEY `id_venta_UNIQUE` (`id_salida_producto`),
  KEY `id_usuario_ibfk_v_idx` (`id_usuario`),
  KEY `id_cliente_ibgk_v_idx` (`id_cliente`),
  KEY `id_factura_ibfk_v_idx` (`id_factura`),
  CONSTRAINT `id_cliente_ibfk_v` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_entidad`),
  CONSTRAINT `id_factura_ibfk_v` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`),
  CONSTRAINT `id_salida_producto_ibfk_v` FOREIGN KEY (`id_salida_producto`) REFERENCES `salida_producto` (`id_salida_producto`),
  CONSTRAINT `id_usuario_ibfk_v` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_entidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,1,1,1,'2020-02-21 08:48:00',2.00,'dev','2022-02-21 08:59:01',1),(2,1,1,1,'2020-02-21 08:48:00',20.50,'dev','2022-02-21 09:04:50',1),(3,1,1,1,'2020-02-21 08:48:00',20.50,'dev','2022-02-21 09:07:50',0);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vi_almacen`
--

DROP TABLE IF EXISTS `vi_almacen`;
/*!50001 DROP VIEW IF EXISTS `vi_almacen`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_almacen` AS SELECT 
 1 AS `id_almacen`,
 1 AS `descripcion`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_cliente`
--

DROP TABLE IF EXISTS `vi_cliente`;
/*!50001 DROP VIEW IF EXISTS `vi_cliente`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_cliente` AS SELECT 
 1 AS `id_entidad`,
 1 AS `razon_social`,
 1 AS `nit_ci`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_compra`
--

DROP TABLE IF EXISTS `vi_compra`;
/*!50001 DROP VIEW IF EXISTS `vi_compra`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_compra` AS SELECT 
 1 AS `id_compra`,
 1 AS `id_usuario`,
 1 AS `id_proveedor`,
 1 AS `monto_total`,
 1 AS `fecha`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_contacto`
--

DROP TABLE IF EXISTS `vi_contacto`;
/*!50001 DROP VIEW IF EXISTS `vi_contacto`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_contacto` AS SELECT 
 1 AS `id_contacto`,
 1 AS `id_entidad`,
 1 AS `fecha_registro`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_contacto_correo`
--

DROP TABLE IF EXISTS `vi_contacto_correo`;
/*!50001 DROP VIEW IF EXISTS `vi_contacto_correo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_contacto_correo` AS SELECT 
 1 AS `id_contacto_correo`,
 1 AS `id_contacto`,
 1 AS `correo`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_contacto_direccion`
--

DROP TABLE IF EXISTS `vi_contacto_direccion`;
/*!50001 DROP VIEW IF EXISTS `vi_contacto_direccion`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_contacto_direccion` AS SELECT 
 1 AS `id_contacto_direccion`,
 1 AS `id_contacto`,
 1 AS `id_localidad`,
 1 AS `calle`,
 1 AS `numero_casa`,
 1 AS `zona`,
 1 AS `detalles`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_contacto_telefono`
--

DROP TABLE IF EXISTS `vi_contacto_telefono`;
/*!50001 DROP VIEW IF EXISTS `vi_contacto_telefono`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_contacto_telefono` AS SELECT 
 1 AS `id_contacto_telefono`,
 1 AS `id_contacto`,
 1 AS `codigo_pais`,
 1 AS `numero`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_detalle_entrada`
--

DROP TABLE IF EXISTS `vi_detalle_entrada`;
/*!50001 DROP VIEW IF EXISTS `vi_detalle_entrada`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_detalle_entrada` AS SELECT 
 1 AS `id_detalle_entrada`,
 1 AS `id_compra`,
 1 AS `id_producto`,
 1 AS `cantidad`,
 1 AS `precio_unidad`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_detalle_salida`
--

DROP TABLE IF EXISTS `vi_detalle_salida`;
/*!50001 DROP VIEW IF EXISTS `vi_detalle_salida`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_detalle_salida` AS SELECT 
 1 AS `id_detalle_salida`,
 1 AS `id_salida_producto`,
 1 AS `id_producto`,
 1 AS `cantidad`,
 1 AS `precio_unidad`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_disposicion`
--

DROP TABLE IF EXISTS `vi_disposicion`;
/*!50001 DROP VIEW IF EXISTS `vi_disposicion`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_disposicion` AS SELECT 
 1 AS `id_salida_producto`,
 1 AS `id_usuario`,
 1 AS `id_motivo`,
 1 AS `comentario`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_factura`
--

DROP TABLE IF EXISTS `vi_factura`;
/*!50001 DROP VIEW IF EXISTS `vi_factura`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_factura` AS SELECT 
 1 AS `id_factura`,
 1 AS `codigo_control`,
 1 AS `datos_codigo_QR`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_localidad`
--

DROP TABLE IF EXISTS `vi_localidad`;
/*!50001 DROP VIEW IF EXISTS `vi_localidad`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_localidad` AS SELECT 
 1 AS `id_localidad`,
 1 AS `id_departamento`,
 1 AS `nombre_localidad`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_motivo`
--

DROP TABLE IF EXISTS `vi_motivo`;
/*!50001 DROP VIEW IF EXISTS `vi_motivo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_motivo` AS SELECT 
 1 AS `id_motivo`,
 1 AS `descripcion_motivo`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_presentacion_producto`
--

DROP TABLE IF EXISTS `vi_presentacion_producto`;
/*!50001 DROP VIEW IF EXISTS `vi_presentacion_producto`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_presentacion_producto` AS SELECT 
 1 AS `id_presentacion_producto`,
 1 AS `id_unidad_presentacion`,
 1 AS `nombre_presentacion`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_producto`
--

DROP TABLE IF EXISTS `vi_producto`;
/*!50001 DROP VIEW IF EXISTS `vi_producto`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_producto` AS SELECT 
 1 AS `id_producto`,
 1 AS `id_presentacion_producto`,
 1 AS `nombre`,
 1 AS `codigo`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_producto_almacen`
--

DROP TABLE IF EXISTS `vi_producto_almacen`;
/*!50001 DROP VIEW IF EXISTS `vi_producto_almacen`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_producto_almacen` AS SELECT 
 1 AS `id_producto_almacen`,
 1 AS `id_almacen`,
 1 AS `id_producto`,
 1 AS `stock_actual`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_proveedor`
--

DROP TABLE IF EXISTS `vi_proveedor`;
/*!50001 DROP VIEW IF EXISTS `vi_proveedor`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_proveedor` AS SELECT 
 1 AS `id_entidad`,
 1 AS `nombre`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_unidad_presentacion`
--

DROP TABLE IF EXISTS `vi_unidad_presentacion`;
/*!50001 DROP VIEW IF EXISTS `vi_unidad_presentacion`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_unidad_presentacion` AS SELECT 
 1 AS `id_unidad_presentacion`,
 1 AS `nombre_medida`,
 1 AS `multiplicador_kg`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_usuario`
--

DROP TABLE IF EXISTS `vi_usuario`;
/*!50001 DROP VIEW IF EXISTS `vi_usuario`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_usuario` AS SELECT 
 1 AS `id_entidad`,
 1 AS `id_nivel`,
 1 AS `login_usuario`,
 1 AS `password_usuario`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_usuario_nivel`
--

DROP TABLE IF EXISTS `vi_usuario_nivel`;
/*!50001 DROP VIEW IF EXISTS `vi_usuario_nivel`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_usuario_nivel` AS SELECT 
 1 AS `id_entidad`,
 1 AS `login`,
 1 AS `password_usr`,
 1 AS `id_nivel`,
 1 AS `nivel`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_venta`
--

DROP TABLE IF EXISTS `vi_venta`;
/*!50001 DROP VIEW IF EXISTS `vi_venta`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vi_venta` AS SELECT 
 1 AS `id_salida_producto`,
 1 AS `id_usuario`,
 1 AS `id_cliente`,
 1 AS `id_factura`,
 1 AS `fecha`,
 1 AS `monto_total`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vi_almacen`
--

/*!50001 DROP VIEW IF EXISTS `vi_almacen`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_almacen` AS select `almacen`.`id_almacen` AS `id_almacen`,`almacen`.`descripcion` AS `descripcion` from `almacen` where (`almacen`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_cliente`
--

/*!50001 DROP VIEW IF EXISTS `vi_cliente`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_cliente` AS select `cliente`.`id_entidad` AS `id_entidad`,`cliente`.`razon_social` AS `razon_social`,`cliente`.`nit_ci` AS `nit_ci` from `cliente` where (`cliente`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_compra`
--

/*!50001 DROP VIEW IF EXISTS `vi_compra`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_compra` AS select `compra`.`id_compra` AS `id_compra`,`compra`.`id_usuario` AS `id_usuario`,`compra`.`id_proveedor` AS `id_proveedor`,`compra`.`monto_total` AS `monto_total`,`compra`.`fecha` AS `fecha` from `compra` where (`compra`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_contacto`
--

/*!50001 DROP VIEW IF EXISTS `vi_contacto`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_contacto` AS select `contacto`.`id_contacto` AS `id_contacto`,`contacto`.`id_entidad` AS `id_entidad`,`contacto`.`fecha_registro` AS `fecha_registro` from `contacto` where (`contacto`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_contacto_correo`
--

/*!50001 DROP VIEW IF EXISTS `vi_contacto_correo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_contacto_correo` AS select `contacto_correo`.`id_contacto_correo` AS `id_contacto_correo`,`contacto_correo`.`id_contacto` AS `id_contacto`,`contacto_correo`.`correo` AS `correo` from `contacto_correo` where (`contacto_correo`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_contacto_direccion`
--

/*!50001 DROP VIEW IF EXISTS `vi_contacto_direccion`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_contacto_direccion` AS select `contacto_direccion`.`id_contacto_direccion` AS `id_contacto_direccion`,`contacto_direccion`.`id_contacto` AS `id_contacto`,`contacto_direccion`.`id_localidad` AS `id_localidad`,`contacto_direccion`.`calle` AS `calle`,`contacto_direccion`.`numero_casa` AS `numero_casa`,`contacto_direccion`.`zona` AS `zona`,`contacto_direccion`.`detalles` AS `detalles` from `contacto_direccion` where (`contacto_direccion`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_contacto_telefono`
--

/*!50001 DROP VIEW IF EXISTS `vi_contacto_telefono`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_contacto_telefono` AS select `contacto_telefono`.`id_contacto_telefono` AS `id_contacto_telefono`,`contacto_telefono`.`id_contacto` AS `id_contacto`,`contacto_telefono`.`codigo_pais` AS `codigo_pais`,`contacto_telefono`.`numero` AS `numero` from `contacto_telefono` where (`contacto_telefono`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_detalle_entrada`
--

/*!50001 DROP VIEW IF EXISTS `vi_detalle_entrada`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_detalle_entrada` AS select `detalle_entrada`.`id_detalle_entrada` AS `id_detalle_entrada`,`detalle_entrada`.`id_compra` AS `id_compra`,`detalle_entrada`.`id_producto` AS `id_producto`,`detalle_entrada`.`cantidad` AS `cantidad`,`detalle_entrada`.`precio_unidad` AS `precio_unidad` from `detalle_entrada` where (`detalle_entrada`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_detalle_salida`
--

/*!50001 DROP VIEW IF EXISTS `vi_detalle_salida`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_detalle_salida` AS select `detalle_salida`.`id_detalle_salida` AS `id_detalle_salida`,`detalle_salida`.`id_salida_producto` AS `id_salida_producto`,`detalle_salida`.`id_producto` AS `id_producto`,`detalle_salida`.`cantidad` AS `cantidad`,`detalle_salida`.`precio_unidad` AS `precio_unidad` from `detalle_salida` where (`detalle_salida`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_disposicion`
--

/*!50001 DROP VIEW IF EXISTS `vi_disposicion`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_disposicion` AS select `disposicion`.`id_salida_producto` AS `id_salida_producto`,`disposicion`.`id_usuario` AS `id_usuario`,`disposicion`.`id_motivo` AS `id_motivo`,`disposicion`.`comentario` AS `comentario` from `disposicion` where (`disposicion`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_factura`
--

/*!50001 DROP VIEW IF EXISTS `vi_factura`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_factura` AS select `factura`.`id_factura` AS `id_factura`,`factura`.`codigo_control` AS `codigo_control`,`factura`.`datos_codigo_QR` AS `datos_codigo_QR` from `factura` where (`factura`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_localidad`
--

/*!50001 DROP VIEW IF EXISTS `vi_localidad`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_localidad` AS select `localidad`.`id_localidad` AS `id_localidad`,`localidad`.`id_departamento` AS `id_departamento`,`localidad`.`nombre_localidad` AS `nombre_localidad` from `localidad` where (`localidad`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_motivo`
--

/*!50001 DROP VIEW IF EXISTS `vi_motivo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_motivo` AS select `motivo`.`id_motivo` AS `id_motivo`,`motivo`.`descripcion_motivo` AS `descripcion_motivo` from `motivo` where (`motivo`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_presentacion_producto`
--

/*!50001 DROP VIEW IF EXISTS `vi_presentacion_producto`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_presentacion_producto` AS select `presentacion_producto`.`id_presentacion_producto` AS `id_presentacion_producto`,`presentacion_producto`.`id_unidad_presentacion` AS `id_unidad_presentacion`,`presentacion_producto`.`nombre_presentacion` AS `nombre_presentacion` from `presentacion_producto` where (`presentacion_producto`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_producto`
--

/*!50001 DROP VIEW IF EXISTS `vi_producto`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_producto` AS select `producto`.`id_producto` AS `id_producto`,`producto`.`id_presentacion_producto` AS `id_presentacion_producto`,`producto`.`nombre` AS `nombre`,`producto`.`codigo` AS `codigo` from `producto` where (`producto`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_producto_almacen`
--

/*!50001 DROP VIEW IF EXISTS `vi_producto_almacen`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_producto_almacen` AS select `producto_almacen`.`id_producto_almacen` AS `id_producto_almacen`,`producto_almacen`.`id_almacen` AS `id_almacen`,`producto_almacen`.`id_producto` AS `id_producto`,`producto_almacen`.`stock_actual` AS `stock_actual` from `producto_almacen` where (`producto_almacen`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_proveedor`
--

/*!50001 DROP VIEW IF EXISTS `vi_proveedor`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_proveedor` AS select `proveedor`.`id_entidad` AS `id_entidad`,`proveedor`.`nombre` AS `nombre` from `proveedor` where (`proveedor`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_unidad_presentacion`
--

/*!50001 DROP VIEW IF EXISTS `vi_unidad_presentacion`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_unidad_presentacion` AS select `unidad_presentacion`.`id_unidad_presentacion` AS `id_unidad_presentacion`,`unidad_presentacion`.`nombre_medida` AS `nombre_medida`,`unidad_presentacion`.`multiplicador_kg` AS `multiplicador_kg` from `unidad_presentacion` where (`unidad_presentacion`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_usuario`
--

/*!50001 DROP VIEW IF EXISTS `vi_usuario`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_usuario` AS select `usuario`.`id_entidad` AS `id_entidad`,`usuario`.`id_nivel` AS `id_nivel`,`usuario`.`login_usuario` AS `login_usuario`,`usuario`.`password_usuario` AS `password_usuario` from `usuario` where (`usuario`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_usuario_nivel`
--

/*!50001 DROP VIEW IF EXISTS `vi_usuario_nivel`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_usuario_nivel` AS select `usuario`.`id_entidad` AS `id_entidad`,`usuario`.`login_usuario` AS `login`,`usuario`.`password_usuario` AS `password_usr`,`nivel`.`id_nivel` AS `id_nivel`,`nivel`.`nivel` AS `nivel` from (`usuario` join `nivel` on((`usuario`.`id_nivel` = `nivel`.`id_nivel`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_venta`
--

/*!50001 DROP VIEW IF EXISTS `vi_venta`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_venta` AS select `venta`.`id_salida_producto` AS `id_salida_producto`,`venta`.`id_usuario` AS `id_usuario`,`venta`.`id_cliente` AS `id_cliente`,`venta`.`id_factura` AS `id_factura`,`venta`.`fecha` AS `fecha`,`venta`.`monto_total` AS `monto_total` from `venta` where (`venta`.`es_registro_activo` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-09 14:55:33
