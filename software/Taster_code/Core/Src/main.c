/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2026 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stm32f4xx.h" 
#include <stdint.h>
#include <stdio.h>


/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */


/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART2_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
int __io_putchar(int ch)
{
    HAL_UART_Transmit(&huart2, (uint8_t*)&ch, 1, HAL_MAX_DELAY);
    return ch;
}
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
 volatile uint8_t state = 0;
 volatile uint8_t mode = 0;     // Aktueller Betriebsmodus
int main(void)
{

  /* USER CODE BEGIN 1 */
 
  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */


  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART2_UART_Init();

// Debug-Ausgabe der aktuellen Taktfrequenzen über UART
// Zur Überprüfung der System- und Bus-Taktkonfiguration
  printf("SystemCoreClock = %lu\r\n", SystemCoreClock); // CPU-Systemtakt (SYSCLK)
  printf("PCLK1 = %lu\r\n", HAL_RCC_GetPCLK1Freq()); // APB1-Peripherietakt (z. B. TIM2, TIM5)
  printf("PCLK2 = %lu\r\n", HAL_RCC_GetPCLK2Freq()); // APB2-Peripherietakt
  /* USER CODE BEGIN 2 */
// Clock aktivieren
RCC->AHB1ENR |= (1 << 0); // GPIOA
RCC->AHB1ENR |= (1 << 2); // GPIOC

// ----------------------
// TIM2 konfigurieren (1ms Tick)
// ----------------------
// TIM2 Clock aktivieren
RCC->APB1ENR |= (1 << 0);
/// ----------------------
// TIM5 Zeitbasis
// ----------------------
RCC->APB1ENR |= (1 << 3);

TIM5->PSC = 84000 - 1;      // 1 ms
TIM5->ARR = 0xFFFFFFFF; // autoreload

TIM5->EGR = 1;              // <<< wichtig
TIM5->SR = 0;
TIM5->CNT = 0;

TIM5->CR1 = 1;

// =====================================================
// Timer-Konfiguration
// Requirement: TIMER_CONFIGURATION
// TIM2 erzeugt eine periodische Zeitbasis.
//
// @satisfies TIMER_CONFIGURATION
// =====================================================


// 84 MHz und 1s
TIM2->PSC = 84000 - 1;
TIM2->ARR = 1000-1 ;   // 0,5 s  autoreload

TIM2->EGR = 1;          // Werte sofort übernehmen
TIM2->SR = 0;           // Flags löschen
TIM2->CNT = 0;          // Zähler auf 0
// Timer starten
TIM2->CR1 |= (1 << 0);

// ----------------------
// LED ( PC0)
// ----------------------

// ----------------------

// =====================================================
// GPIO-Konfiguration
// Requirement: GPIO_CONFIG
// PA11–PA14 als Eingänge
// PC0–PC3 als Ausgänge
//
// @satisfies GPIO_CONFIG
// =====================================================

GPIOC->MODER &= ~(0xFF);   // reset PC0–PC3
GPIOC->MODER |=  (0x55);   // output

// ----------------------
// Taster PA11–PA14 Input
// ----------------------
GPIOA->MODER &= ~(0xFF << 22); // reset PA11–PA14

// =====================================================
// Tasterlogik
// Requirement: TASTER_LOGIC
// Active-Low Eingänge mit Pull-Up
//
// @satisfies TASTER_LOGIC
// =====================================================

// Pull-Up für alle
GPIOA->PUPDR &= ~(0xFF << 22);
GPIOA->PUPDR |=  (0x55 << 22); // Pull-Up
  /* USER CODE END 2 */

  /* Infinite loop */

  /* USER CODE BEGIN WHILE */
  while (1)
{
      // -----------------------------
    // Taster prüfen
    // -----------------------------

    // Taster 1 gedrückt
    if (!(GPIOA->IDR & (1 << 11)))
    {
        mode = 1;
    }

    // Taster 2 gedrückt
    else if (!(GPIOA->IDR & (1 << 12)))
    {
        mode = 2;
    }

    // Taster 3 gedrückt
    else if (!(GPIOA->IDR & (1 << 13)))
    {
        mode = 3;
    }

    // Taster 4 gedrückt
    else if (!(GPIOA->IDR & (1 << 14)))
    {
        mode = 4;
    }

    // --------------------------------
    // Timer ist abgelaufen?
    // --------------------------------
    if (TIM2->SR & 1)
    {
        // Update-Flag löschen
        TIM2->SR &= ~(1 << 0);

        switch (mode)
        {
  // =====================================================
// Requirement: TASTER_1_FUNCTION
// Requirement: T1_TIMING
//
// @satisfies TASTER_1_FUNCTION
// @satisfies T1_TIMING
// =====================================================

            // -------------------------
            // Modus 1
            // LED1 blinkt
            // -------------------------
            case 1:
                GPIOC->ODR ^= (1 << 0);      // PC0 umschalten
                GPIOC->ODR &= ~0x0E;         // PC1-PC3 ausschalten
               printf("LED1 TOGGLE %lu\r\n", TIM5->CNT);

                break;

// =====================================================
// Requirement: TASTER_2_FUNCTION
// Requirement: T2_TIMING
//
// @satisfies TASTER_2_FUNCTION
// @satisfies T2_TIMING
// =====================================================           

            // -------------------------
            // Modus 2
            // LED2 blinkt
            // -------------------------
            case 2:
                GPIOC->ODR ^= (1 << 1);      // PC1 umschalten
                GPIOC->ODR &= ~0x0D;         // PC0,PC2,PC3 aus
                printf("LED2 TOGGLE %lu\r\n", TIM5->CNT);

                break;

// =====================================================
// Requirement: TASTER_3_FUNCTION
//
// @satisfies TASTER_3_FUNCTION
// =====================================================        

            // -------------------------
            // Modus 3
            // Alle LEDs blinken
            // -------------------------
            case 3:
                GPIOC->ODR ^= 0x0F;
                printf("ALL TOGGLE %lu\r\n", TIM5->CNT);
                break;
// =====================================================
// Requirement: TASTER_4_FUNCTION
//
// @satisfies TASTER_4_FUNCTION
// =====================================================


            // -------------------------
            // Modus 4
            // Alle LEDs dauerhaft an
            // -------------------------
            case 4:
                GPIOC->ODR = 0x0F;
                printf("ALL ON %lu\r\n", TIM5->CNT);
                break;

            // -------------------------
            // Kein Modus gewählt
            // -------------------------
            default:
                GPIOC->ODR = 0x00;
                break;
        }
    }
}
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE3);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 16;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 2;
  RCC_OscInitStruct.PLL.PLLR = 2;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 115200;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  /* USER CODE BEGIN MX_GPIO_Init_1 */

  /* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : B1_Pin */
  GPIO_InitStruct.Pin = B1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(B1_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : LD2_Pin */
  GPIO_InitStruct.Pin = LD2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(LD2_GPIO_Port, &GPIO_InitStruct);

  /* USER CODE BEGIN MX_GPIO_Init_2 */

  /* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}
#ifdef USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

