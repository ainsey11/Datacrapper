<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit6aa80c464f929d1c0f02a17a0eab8d08
{
    public static $prefixesPsr0 = array (
        'P' => 
        array (
            'PEAR2\\Net\\Transmitter\\' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/net_transmitter/src',
                1 => __DIR__ . '/..' . '/pear2/net_routeros/vendor/pear2/net_transmitter/src',
            ),
            'PEAR2\\Net\\RouterOS\\' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/net_routeros/src',
            ),
            'PEAR2\\Console\\Color' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/net_routeros/vendor/pear2/console_color/src',
            ),
            'PEAR2\\Cache\\SHM' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/net_routeros/vendor/pear2/cache_shm/src',
            ),
        ),
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixesPsr0 = ComposerStaticInit6aa80c464f929d1c0f02a17a0eab8d08::$prefixesPsr0;

        }, null, ClassLoader::class);
    }
}
