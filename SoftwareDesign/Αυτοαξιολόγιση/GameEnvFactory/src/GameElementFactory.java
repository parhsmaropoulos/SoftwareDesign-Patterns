package GameEnvFactory.src;

/**
 * Declares an interface for operations that create abstract game enviroment
 * objects.
 */
public interface GameElementFactory {
    SinglePlayer createSinglePlayer();

    MultiPlayer createMultiPlayer();

    FPSgame createFPSgame();

    MOBA createMoba();

}